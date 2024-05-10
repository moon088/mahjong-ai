#特徴量作成:数牌の|数字-5|の枚数　<-内側の数牌がどれほど手牌にあるか

def calculate_kazuhai_feature(hand,dora):
    if len(hand) != 13:
        return "error"
    absolute_m = [4,3,2,1,0,1,2,3,4]
    absolute_s = [4,3,2,1,0,1,2,3,4]
    absolute_p = [4,3,2,1,0,1,2,3,4]
    #絶対値-4の配列
    absolute_3col = [absolute_m,absolute_p,absolute_s]
    
    #枚数の配列
    count_m = [0] * 9
    count_p = [0] * 9
    count_s = [0] * 9
    count_3col = [count_m,count_p,count_s]
    for hai in hand:
        if hai.startswith("m"):
            count_3col[0][int(hai[1])-1]  += 1
        elif hai.startswith("p"):
            count_3col[1][int(hai[1])-1]  += 1
        elif hai.startswith("s"):
            count_3col[2][int(hai[1])-1]  += 1    
    #print(count_3col)    

    #isDoraの配列
    isDora_m = [0] * 9
    isDora_p = [0] * 9
    isDora_s = [0] * 9
    isDora_3col = [isDora_m,isDora_p,isDora_s]
    
    if dora.startswith("m"):
        isDora_3col[0][int(dora[1])-1]  += 1
    elif dora.startswith("p"):
        isDora_3col[1][int(dora[1])-1]  += 1
    elif dora.startswith("s"):
        isDora_3col[2][int(dora[1])-1]  += 1
    #print(isDora_3col)
    return [absolute_3col,count_3col,isDora_3col]
    
    
#test
#hand = ['m1','m1','m4','m7','p1','p2','p5','p6','s1','s5','s7','s7','s9']
#dora = 'p3'
#result = calculate_kazuhai_feature(hand,dora)
#print(result)
        
