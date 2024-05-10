#特徴量作成:国士無双の向聴数

def calculate_kokushimusou_shanten(hand):
    def calculate_kokushimusou_shanten_sub(hand):
        if len(hand) != 13:
            return "error"
        #1,9,字牌の種類をカウントする
        count_yaochuhai = 0
        #それぞれm1,m9,s1,s9,p1,p9,z1~z7の枚数
        yaochuhai = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        #1,9,字牌のトイツがあるか
        exist_toitsu = False

        for hai in hand:
            if(hai == 'm1'):
                yaochuhai[0] += 1
            elif(hai == 'm9'):
                yaochuhai[1] += 1
            elif(hai == 's1'):
                yaochuhai[2] += 1
            elif(hai == 's9'):
                yaochuhai[3] += 1
            elif(hai == 'p1'):
                yaochuhai[4] += 1
            elif(hai == 'p9'):
                yaochuhai[5] += 1
            elif(hai == 'z1'):
                yaochuhai[6] += 1
            elif(hai == 'z2'):
                yaochuhai[7] += 1
            elif(hai == 'z3'):
                yaochuhai[8] += 1
            elif(hai == 'z4'):
                yaochuhai[9] += 1
            elif(hai == 'z5'):
                yaochuhai[10] += 1
            elif(hai == 'z6'):
                yaochuhai[11] += 1
            elif(hai == 'z7'):
                yaochuhai[12] += 1

        for num in yaochuhai:
            if num > 0:
                count_yaochuhai += 1

            if num >= 2:
                exist_toitsu = True
        if exist_toitsu:
            shanten = 13 - count_yaochuhai - 1
        else:
            shanten = 13 - count_yaochuhai 
        
        return shanten
    return calculate_kokushimusou_shanten_sub(hand)

#test
#hand = ['m1','m1','s1','s9','p1','p1','z1','z1','z3','z4','z5','z6','z7']
#print(calculate_kokushimusou_shanten(hand))