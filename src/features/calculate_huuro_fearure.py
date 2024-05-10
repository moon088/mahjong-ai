#特徴量作成:副露数

def calculate_huuro_feature(hand):
    tehai = hand[0]
    huuro = hand[1]
    return len(huuro) // 3

#hand = [['m1','m1','s1','s9','p1','p1','z1'],['s1','s1','s1','s9','s9','s9']]
#result = calculate_huuro_feature(hand)
#print(result)