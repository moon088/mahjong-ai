import os
import xml.etree.ElementTree as ET

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
        dora_indicator = seed[5] if len(seed) > 5 else 'NULL'

        reach_found = False
        for elem in elements_between:
            if elem.tag == 'REACH' and elem.get('step') == '1':
                player_number = elem.get('who')
                reach_found = True
                break
            elif elem.tag[0] in 'TUVWDEFG':
                discards.append(elem.tag + elem.text if elem.text else elem.tag)

        if reach_found:
            results.append({
                f'hai{player_number}': player_hands[f'hai{player_number}'],
                'discards_before_reach': discards
            })

    return results  # 最後に結果リストを返す

directory_path = r''

all_results = []

if __name__ == "__main__":
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory_path, filename)
            all_results.extend(analyze_xml(file_path))

    # 全ての結果をリストとして出力(print)
    print(all_results)
