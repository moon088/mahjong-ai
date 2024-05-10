#特徴量作成:役牌の数

def calculate_yakuhai_feature(hand,bakaze,jikaze,dora):
    if len(hand) != 13:
        return "error"
    number_of_zihai = [0,0,0,0,0,0,0]
    number_of_yaku = [0,0,0,0,1,1,1]
    dora_or_not = [0,0,0,0,0,0,0]

    if bakaze == 'z1':
        number_of_yaku[0] += 1
    elif bakaze == 'z2':
        number_of_yaku[1] += 1
    elif bakaze == 'z3':
        number_of_yaku[2] += 1
    elif bakaze == 'z4':
        number_of_yaku[3] += 1

    if jikaze == 'z1':
        number_of_yaku[0] += 1
    elif jikaze == 'z2':
        number_of_yaku[1] += 1
    elif jikaze == 'z3':
        number_of_yaku[2] += 1
    elif jikaze == 'z4':
        number_of_yaku[3] += 1

    if dora == 'z1':
        dora_or_not[0] = 1
    elif dora == 'z2':
        dora_or_not[1] = 1
    elif dora == 'z3':
        dora_or_not[2] = 1
    elif dora == 'z4':
        dora_or_not[3] = 1
    elif dora == 'z5':
        dora_or_not[4] = 1
    elif dora == 'z6':
        dora_or_not[5] = 1
    elif dora == 'z7':
        dora_or_not[6] = 1


    for hai in hand:
        if(hai == 'z1'):
            number_of_zihai[0] += 1
        elif(hai == 'z2'):
            number_of_zihai[1] += 1
        elif(hai == 'z3'):
            number_of_zihai[2] += 1
        elif(hai == 'z4'):
            number_of_zihai[3] += 1
        elif(hai == 'z5'):
            number_of_zihai[4] += 1
        elif(hai == 'z6'):
            number_of_zihai[5] += 1
        elif(hai == 'z7'):
            number_of_zihai[6] += 1
    
    return number_of_zihai,number_of_yaku,dora_or_not 

#hand = ['m1','m1','m1','m9','p1','p1','s1','s1','s2','z1','z1','z5','z6']
#result = calculate_yakuhai_feature(hand,'z1','z1','z3')
# print(result)
#for num in range(7):
#print("z",num+1,": ",result[0][num],"枚 ",result[1][num],"翻 ドラ",result[2][num])
