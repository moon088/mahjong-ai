#特徴量作成:手牌における数牌2~8の枚数

def calculate_colors_feature(hand):
    if len(hand) != 13:
        return "error"
    count_2to8 = 0
    for hai in hand:
        if hai != 'm1' and hai != 'm9' and hai != 's1' and hai != 's9' and hai != 'p1' and hai != 'p9' and hai != 'z1' and hai != 'z2' and hai != 'z3' and hai != 'z4' and hai != 'z5' and hai != 'z6' and hai != 'z7':
            count_2to8 += 1
    return count_2to8

#test
#hand = ['m1','m1','s2','s9','p1','p1','z1','z1','z3','z4','z5','z6','z7']
#result = calculate_colors_feature(hand)
#print(result)