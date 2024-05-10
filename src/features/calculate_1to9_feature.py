#特徴量作成:手牌における数牌1~9の枚数

def calculate_1to9_feature(hand):
    if len(hand) != 13:
        return "error"
    ex_of_m = [0,0,0,0,0,0,0,0,0]
    ex_of_p = [0,0,0,0,0,0,0,0,0]
    ex_of_s = [0,0,0,0,0,0,0,0,0]

    for hai in hand:
        if(hai == 'm1'):
            ex_of_m[0] += 1
        elif(hai == 'm2'):
            ex_of_m[1] += 1
        elif(hai == 'm3'):
            ex_of_m[2] += 1
        elif(hai == 'm4'):
            ex_of_m[3] += 1
        elif(hai == 'm5'):
            ex_of_m[4] += 1
        elif(hai == 'm6'):
            ex_of_m[5] += 1
        elif(hai == 'm7'):
            ex_of_m[6] += 1
        elif(hai == 'm8'):
            ex_of_m[7] += 1
        elif(hai == 'm9'):
            ex_of_m[8] += 1
      
    for hai in hand:
        if(hai == 'p1'):
            ex_of_p[0] += 1
        elif(hai == 'p2'):
            ex_of_p[1] += 1
        elif(hai == 'p3'):
            ex_of_p[2] += 1
        elif(hai == 'p4'):
            ex_of_p[3] += 1
        elif(hai == 'p5'):
          ex_of_p[4] += 1
        elif(hai == 'p6'):
            ex_of_p[5] += 1
        elif(hai == 'p7'):
            ex_of_p[6] += 1
        elif(hai == 'p8'):
            ex_of_p[7] += 1
        elif(hai == 'p9'):
            ex_of_p[8] += 1

    for hai in hand:
        if(hai == 's1'):
            ex_of_s[0] += 1
        elif(hai == 's2'):
            ex_of_s[1] += 1
        elif(hai == 's3'):
            ex_of_s[2] += 1
        elif(hai == 's4'):
            ex_of_s[3] += 1
        elif(hai == 's5'):
            ex_of_s[4] += 1
        elif(hai == 's6'):
            ex_of_s[5] += 1
        elif(hai == 's7'):
            ex_of_s[6] += 1
        elif(hai == 's8'):
            ex_of_s[7] += 1
        elif(hai == 's9'):
            ex_of_s[8] += 1
    
    ex_of_3col = [[],[],[]]
    ex_of_3col[0] = ex_of_m
    ex_of_3col[1] = ex_of_p
    ex_of_3col[2] = ex_of_s
    
    for k_col in range(len(ex_of_3col)):
        for k_hai in range(len(ex_of_3col[k_col])):
            if ex_of_3col[k_col][k_hai] >= 1:
                ex_of_3col[k_col][k_hai] = 1    
    
    return ex_of_3col

#test
hand = ['m1','m1','s1','s9','p1','p1','z1','z1','z3','z4','z5','z6','z7']
print(calculate_1to9_feature(hand))