#初期手配から捨て牌・自模り牌情報を用いて更新手牌を出力

def print_updated_hands(initial_hand, discards, x):
    hand_tiles = initial_hand.copy()  # 初期手牌のコピーを作成
    updated_hands = []
    add_char = ['T', 'U', 'V', 'W'][x]
    remove_char = ['D', 'E', 'F', 'G'][x]

    for discard in discards:
        # もし指定された文字で始まるならば、その牌を手牌に追加する
        if discard.startswith(add_char):
            tile = int(discard[1:])  
            hand_tiles.append(tile)  
            updated_hands.append(hand_tiles.copy())  # 現在の手牌を記録
        # もし指定された削除の文字で始まるならば、その牌を手牌から削除する
        elif discard.startswith(remove_char):
            tile = int(discard[1:])  
            if tile in hand_tiles:
                hand_tiles.remove(tile)  

    # 更新された手牌のリストのリストを返す
    return updated_hands


initial_hand = [91, 124, 49, 2, 59, 44, 100, 32, 77, 63, 29, 27, 76]
discards = ['T135', 'D2', 'U51', 'E118', 'V41', 'F73', 'W93', 'G37', 'T115', 'D115', 'U70', 'E105', 'V109', 'F30', 'W47', 'G110', 'F125', 'W72', 'G72', 'T54', 'D124', 'U1', 'E70', 'F90', 'W98', 'G126', 'T97', 'D135', 'U55', 'E133', 'V9', 'F102', 'W71', 'G121', 'T106']
x = 0

if __name__ == "__main__":
    updated_hands_list = print_updated_hands(initial_hand, discards, x)
    print(updated_hands_list)  # 更新された手牌のリストのリストを出力
