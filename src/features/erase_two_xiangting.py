#一人用麻雀作成において、２色を消したときの向聴数の計算。マンズとピンズだけ消した場合

def dazi(pai):
    n_pai, n_dazi = 0, 0
    for i in range(9):
        n_pai += pai[i]
        if i < 7 and pai[i + 1] == 0 and pai[i + 2] == 0:
            n_dazi += n_pai // 2 #
            n_pai = 0  #リセット
    n_dazi += n_pai // 2 
    return n_dazi

def mianzi(pai, n):
    if n == 9: #面子抜き終わったターツの数カウント
        dazi_count = dazi(pai)
        return [[0, dazi_count], [0, dazi_count]]

    max_mianzi = mianzi(pai[:], n + 1)

    #以下のif文では、順子を抜き取っている。nは位置を表している。
    if n < 7 and pai[n] > 0 and pai[n + 1] > 0 and pai[n + 2] > 0:
        pai_copy = pai[:]
        pai_copy[n] -= 1
        pai_copy[n + 1] -= 1
        pai_copy[n + 2] -= 1
        r = mianzi(pai_copy, n) 
        pai_copy[n] += 1
        pai_copy[n+1] += 1
        pai_copy[n+2] += 1
        #元に戻した。
        r[0][0] += 1
        r[1][0] += 1
        if r[0][0] * 2 + r[0][1] > max_mianzi[0][0] * 2 + max_mianzi[0][1]:
          max_mianzi[0] = r[0]
        if r[1][0] * 10 + r[1][1] > max_mianzi[1][0] * 10 + max_mianzi[1][1]:
          max_mianzi[1] = r[1] 
            

    if pai[n] >= 3:
        pai_copy = pai[:]
        pai_copy[n] -= 3
        r = mianzi(pai_copy, n) 
        pai_copy[n] += 3        
        r[0][0] += 1
        r[1][0] += 1
        if r[0][0] * 2 + r[0][1] > max_mianzi[0][0] * 2 + max_mianzi[0][1]:
          max_mianzi[0] = r[0]
        if r[1][0] * 10 + r[1][1] > max_mianzi[1][0] * 10 + max_mianzi[1][1]:
          max_mianzi[1] = r[1]
    #print(max_mianzi)
    return max_mianzi

def mianzi_all(shoupai):
    mianzi_counts = {}
    for s in ['m', 'p', 's']:
        mianzi_counts[s] = mianzi(shoupai[s], 0)

    # 字牌の面子・搭子の数をカウント -> ここターツじゃなくて対子じゃね。
    z = [0, 0]
    for n in range(7):
        if shoupai['z'][n] >= 3:
            z[0] += 1
        if shoupai['z'][n] == 2:
            z[1] += 1

    # 副露牌の数をカウント（存在しない場合は0とする）。今回は0でいいはず。
    n_fulou = len(shoupai['_fulou']) if '_fulou' in shoupai else 0

    min_xiangting = 8
    for m in mianzi_counts['m']:
        for p in mianzi_counts['p']:
            for s in mianzi_counts['s']:
                total_mianzi = s[0] + z[0] + n_fulou
                total_dazi = s[1] + z[1]
                if total_mianzi + total_dazi > 4:
                  total_dazi = 4 - total_mianzi
                xiangting = 8 - total_mianzi * 2 - total_dazi
                min_xiangting = min(min_xiangting, xiangting)

    return min_xiangting



#メイン
def xiangting(shoupai):
    # 雀頭なしとした場合の向聴数を最小値に仮置き
    min_xiangting = mianzi_all(shoupai)

    # 可能な雀頭を抜き取り mianzi_all() を呼び出し、向聴数を計算させる
    for s in ['m', 'p', 's', 'z']:
        for i in range(len(shoupai[s])):
            if shoupai[s][i] >= 2:
                #print(shoupai[s][i])
                shoupai[s][i] -= 2
                xiangting_val = mianzi_all(shoupai) - 1
                shoupai[s][i] += 2
                min_xiangting = min(min_xiangting, xiangting_val)

    return min_xiangting

#{'m': [0, 0, 1, 0, 1, 0, 0, 0, 1], 'p': [0, 1, 0, 0, 0, 1, 1, 0, 0], 
#          's': [1, 0, 1, 0, 2, 0, 0, 1, 0], 'z': [0, 0, 0, 1, 1, 1, 0]}
#359m267p13558s456zを
#{'m': [0, 0, 1, 0, 1, 0, 0, 0, 1], 'p': [0, 1, 0, 0, 0, 1, 1, 0, 0], 
# 's': [1, 0, 1, 0, 2, 0, 0, 1, 0], 'z': [0, 0, 0, 1, 1, 1, 0]}
#に変換する関数。ここ関係ない

def shoupai(str_hand):
    shoupai_dict = {
        'm': [0] * 9,
        'p': [0] * 9,
        's': [0] * 9,
        'z': [0] * 7
    }

    current_suit = ''
    num_str = ''
    for char in str_hand:
        if char.isdigit():
            num_str += char
        elif char in shoupai_dict:
            if num_str:
                for num in num_str:
                    shoupai_dict[char][int(num) - 1] += 1
                num_str = ''
            current_suit = char

    if num_str and current_suit in shoupai_dict:
        for num in num_str:
            shoupai_dict[current_suit][int(num) - 1] += 1

    return shoupai_dict

#2,4,8,,,を359m,345pの形へ変換する関数ここ関係ない
def convert_to_mahjong_hand(numbers):
    suits = ['m', 'p', 's', 'z']
    hand = {'m': [], 'p': [], 's': [], 'z': []}

    for number in numbers:
        if number < 9:
            hand['m'].append(str(number + 1))
        elif number < 18:
            hand['p'].append(str(number - 8))
        elif number < 27:
            hand['s'].append(str(number - 17))
        else:
            hand['z'].append(str(number - 26))

    hand_str = ''.join([f"{''.join(hand[suit])}{suit}" for suit in suits if hand[suit]])
    return hand_str
    #print((hand_str)) #ここで99m14789p123669とかを出力している。

# Example numbers
#false example 1235899m3345p35s3z -> 色々変えてる。
#numbers = numbers = [8, 8, 9, 12, 15, 16, 17, 18, 19, 20, 23, 23, 23, 26, 1, 8, 5]
#hand_numbers = numbers[:14]
#mahjong_hand = convert_to_mahjong_hand(hand_numbers)
#hand = shoupai(mahjong_hand)
#ここより上は問題ないはず。
#calculated_shanten = xiangting(hand)
# Compare the provided shanten number with the calculated one
#comparison_result = provided_shanten == calculated_shanten
#print(comparison_result, provided_shanten, calculated_shanten, mahjong_hand)