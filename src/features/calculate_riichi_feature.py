#特徴量作成:リーチ可能か否か

import normal_xianting
import convert_haicode

def calculate_riichi_feature(hand):
    tehai = hand[0]
    huuro = hand[1]
    mahjong_hand = convert_haicode.convert_array_to_string(hand)
    syanten_result = normal_xianting.xiangting(normal_xianting.shoupai(mahjong_hand))
    print(syanten_result)
    if(len(huuro) == 0):
        if syanten_result == 0:
            return 1
        else:
            return 0
    else:
        #リーチできない
        return 0
    

#test
#hand = [['m1','m1','s1','s9','p1','p1','z1','s1','s1','s1','s9','s9','s9']]
#result = calculate_riichi_feature(hand)
#print(result)
