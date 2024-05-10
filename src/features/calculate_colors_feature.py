#特徴量作成:最も多い色の数

def calculate_colors_feature(hand):
    if len(hand) != 13:
        return "error"
    
    count_m = 0
    count_s = 0
    count_p = 0

    for hai in hand:
        if hai == 'm1' or hai == 'm2' or hai == 'm3' or hai == 'm4' or hai == 'm5' or hai == 'm6' or hai == 'm7' or hai == 'm8' or hai == 'm9':
            count_m += 1
        elif hai == 's1' or hai == 's2' or hai == 's3' or hai == 's4' or hai == 's5' or hai == 's6' or hai == 's7' or hai == 's8' or hai == 's9':
            count_s += 1
        elif hai == 'p1' or hai == 'p2' or hai == 'p3' or hai == 'p4' or hai == 'p5' or hai == 'p6' or hai == 'p7' or hai == 'p8' or hai == 'p9':
            count_p += 1
    max_msp = max(count_m,count_s,count_p)    
    return max_msp

#test
#hand = ['m1','m1','m1','m9','p1','p1','s1','z1','z2','z3','z4','z5','z6']
#result = calculate_colors_feature(hand)
#print(result)
