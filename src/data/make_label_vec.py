import os
import xml.etree.ElementTree as ET
#ラベルベクトルを生成するコード。

def analyze_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_data = file.read()

    root = ET.fromstring(xml_data)

    results = []  # 結果を格納するリスト

    init_elements = root.findall('.//INIT')

    for i in range(len(init_elements)):
        init = init_elements[i]
        if i < len(init_elements) - 1:
            next_init = init_elements[i+1]
            next_init_index = list(root).index(next_init)
        else:
            next_init_index = len(list(root))

        init_index = list(root).index(init)
        elements_between = list(root)[init_index:next_init_index]

        discards = []
        player_hands = {f"hai{p}": init.get(f"hai{p}") for p in range(4)}
        seed = init.get('seed').split(',')
        dora_indicator = int(seed[5].split(',')[0]) if len(seed) > 5 else 'NULL'

        # 場風の計算と整数値への変換
        oya = int(seed[1])
        ba_kaze_int = [109, 113, 117, 121][oya % 4]

        reach_found = False
        for elem in elements_between:
            if elem.tag == 'REACH' and elem.get('step') == '1':
                player_number = int(elem.get('who'))
                reach_found = True
                break
            elif elem.tag[0] in 'TUVWDEFG':
                discards.append(elem.tag + elem.text if elem.text else elem.tag)

        if reach_found:
            # 自風の計算と整数値への変換
            jikaze_int = [109, 113, 117, 121][(oya + player_number) % 4]

            results.append({
                'player': player_number,
                'initial_hand': [int(x) for x in player_hands[f'hai{player_number}'].split(',')],
                'discards_before_reach': discards,
                'bakaze': ba_kaze_int,
                'jikaze': jikaze_int,
                'dorahai': dora_indicator
            })

    return results

def print_updated_hands(initial_hand, discards, x, bakaze, jikaze, dorahai):
    # 初期手牌に場風、字牌、ドラを追加
    hand_tiles = initial_hand
    fixed_tiles = [bakaze, jikaze, dorahai]

    updated_hands = []

    add_char = ['T', 'U', 'V', 'W'][x]
    remove_char = ['D', 'E', 'F', 'G'][x]

    for discard in discards:
        if discard.startswith(add_char):
            tile = int(discard[1:])
            # 新たに引いた牌を場風、自風、ドラ表示牌の前に挿入
            hand_tiles.append(tile)
            updated_hands.append(hand_tiles.copy() + fixed_tiles)
        elif discard.startswith(remove_char):
            tile = int(discard[1:])
            if tile in hand_tiles:
                hand_tiles.remove(tile)

    return updated_hands

#パスを入力
directory_path = r'' 

def find_discarded_tile_position(prev_hand, current_hand):
    # 無くなった牌を探す
    for tile in prev_hand:
        if tile not in current_hand:
            discarded_tile = tile
            break

    # 無くなった牌の位置を見つける
    position = prev_hand.index(discarded_tile)

    # 14次元ベクトルを生成
    vector = [0] * 14
    vector[position] = 1

    return vector

if __name__ == "__main__":
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory_path, filename)
            game_results = analyze_xml(file_path)
            for result in game_results:
                player = result['player']
                updated_hands_list = print_updated_hands(result['initial_hand'], result['discards_before_reach'], player, result['bakaze'], result['jikaze'], result['dorahai'])

                # 前回の手牌を保存
                prev_hand = None
                for hand in updated_hands_list:
                    if prev_hand is not None:
                        vector = find_discarded_tile_position(prev_hand, hand)
                        print(vector)  # 生成されたベクトルを出力
                    prev_hand = hand
