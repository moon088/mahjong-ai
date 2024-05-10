import numpy as np
import convert_haicode
import normal_xianting
import calculate_titoi_feature
import calculate_kokushimusou_shanten
import erase_one_xiangting
import erase_two_xiangting
import erase_three_xiangting_z
import calculate_colors_feature
import calculate_colorsandzihai_feature
import calculate_2to8_feature
import calculate_yakuhai_fearute
import calculate_kazuhai_feature
import calculate_1to9_feature
import calculate_mentu_feature
import calculate_continuous_feature
import calculate_tanyao_xiangting

hand = ['m1','m1','m4','m7','p1','z1','z1','z1','z1','z3','z7','z7','z7']
bakaze = 'z1'
jikaze = 'z1'
dora = 'p2'

#通常手向聴数変換
def normal_convert(hand):  
    mahjong_hand = convert_haicode.convert_array_to_string(hand)
    normal_result = normal_xianting.xiangting(normal_xianting.shoupai(mahjong_hand))
    normal_dataset = [0] * 10
    normal_dataset[normal_result + 1] = 1 #range-1~8よりインデックスをインクリメント
    return normal_dataset
#test
#print(normal_convert(hand))
print(len(normal_convert(hand)))

#七対子向聴数変換
def titoi_convert(hand):
    titoi_result = calculate_titoi_feature.calculate_titoitu_shanten(hand)
    titoi_dataset = [0] * 7
    titoi_dataset[titoi_result] = 1
    return titoi_dataset
#test
print(len(titoi_convert(hand)))

#国士無双向聴数変換
def kokusi_convert(hand):
    kokusi_result = calculate_kokushimusou_shanten.calculate_kokushimusou_shanten(hand)
    kokusi_dataset = [0] * 14
    kokusi_dataset[kokusi_result] = 1
    return kokusi_dataset
#test
print(len(kokusi_convert(hand))) 

#独自制作特徴量(erase_one_xiangting)変換
def erase_one_convert(hand):
        mahjong_hand = convert_haicode.convert_array_to_string(hand)
        erase_one_result = erase_one_xiangting.xiangting(erase_one_xiangting.shoupai(mahjong_hand))
        #erase_one_resultのrange-1~8
        erase_one_dataset = [0] * 10
        erase_one_dataset[erase_one_result] = 1
        return erase_one_dataset
#test 
print(len(erase_one_convert(hand)))

#独自制作特徴量(erase_two_xiangting)変換
def erase_two_convert(hand):
        mahjong_hand = convert_haicode.convert_array_to_string(hand)
        erase_two_result = erase_two_xiangting.xiangting(erase_two_xiangting.shoupai(mahjong_hand))
        #erase_two_resultのrange-1~8
        erase_two_dataset = [0] * 10
        erase_two_dataset[erase_two_result] = 1
        return erase_two_dataset
#test 
print(len(erase_two_convert(hand)))

#独自制作特徴量(erase_three_xiangting_z)変換
def erase_three_convert(hand):
        mahjong_hand = convert_haicode.convert_array_to_string(hand)
        erase_three_result = erase_three_xiangting_z.xiangting_z(erase_three_xiangting_z.shoupai(mahjong_hand))
        #erase_three_resultのrange-1~8
        erase_three_dataset = [0] * 10
        erase_three_dataset[erase_three_result] = 1
        return erase_three_dataset
#test 
print(len(erase_three_convert(hand)))

#色の中で最も多い色の数変換
def maxcolors_convert(hand):
    maxcolors_result = calculate_colors_feature.calculate_colors_feature(hand)
    #maxcolors_resultのrange4~13だと思うが、論文に合わせて次元数15
    maxcolors_dataset = [0] * 15
    maxcolors_dataset[maxcolors_result] = 1
    return maxcolors_dataset
#test
print(len(maxcolors_convert(hand)))

#色の中で最も多い色+字牌変換
def sumOfColandZihai_convert(hand):
    sum_result = calculate_colorsandzihai_feature.calculate_colorsandzihai_feature(hand)
    sum_dataset = [0] * 15
    sum_dataset[sum_result] = 1
    return sum_dataset
#test
print(len(sumOfColandZihai_convert(hand)) )

#2から8の数変換
def countOf2To8_convert(hand):
    count_result = calculate_2to8_feature.calculate_colors_feature(hand)
    count_dataset = [0] * 15
    count_dataset[count_result] = 1
    return count_dataset
#test
print(len(countOf2To8_convert(hand)) )

#メンツ+両面ターツ+メンツ候補の組み合わせ(独自解釈)の組み合わせ変換
def mentucomb_convert(hand):
        mahjong_hand = convert_haicode.convert_array_to_string(hand)
        hand = calculate_mentu_feature.shoupai(mahjong_hand)
        calculated_shanten = calculate_mentu_feature.xiangting(hand)
        mentu_dataset = [0] * 7 #range0~6
        mentu_dataset[calculated_shanten] = 1
        return mentu_dataset
#test
print(len(mentucomb_convert(hand)))


#1つ下のyakudoraOfzihai_convertのsub関数
def cmbinate_bctor(k,l,m):
    # サイズ３の配列[4,2,1]
    size_array = [5, 3, 2]
    # (k, l, m)の組み合わせの総数
    total_combinations = np.prod(size_array)
    # 新しいサイズ30の初期値がすべて0の配列を作成
    output_array = [0] * 30
    # (k, l, m)の組み合わせに対応するインデックスに1を設定
    for a in range(size_array[0]):
        for b in range(size_array[1]):
            for c in range(size_array[2]):
                if a == k and b == l and c == m:
                    index = a * size_array[1] * size_array[2] + l * size_array[2] + m
                    output_array[index] = 1
    return output_array


#各字牌の枚数と役牌かどうかとドラの組合せの変換(独自解釈)
#これ特徴量5*3*2=60?と論文にあるが、7*5*3*2=210で行う。
#210次元のベクトルは[(z1),(z2),...(z7)]。各z_iは30次元で,それは((所持枚数5次元),(役牌半数3次元),(ドラか2次元))
def yakudoraOfzihai_convert(hand,bakaze,jikaze,dora):
    yakudora_result = calculate_yakuhai_fearute.calculate_yakuhai_feature(hand,bakaze,jikaze,dora) 
    #ex.)print(yakudora_result) = ([4, 0, 1, 0, 0, 0, 1], [2, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0])
    
    # 列ごとに要素を抽出して配列として出力する
    result_array = []
    final_array = []
    for column_values in zip(*yakudora_result):
        result_array.append(list(column_values))
    #ex.)print(result_array) = [[4, 2, 1], [0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
    
    
    for k_zihai in result_array:
        kzihaiOfvector = cmbinate_bctor(k_zihai[0],k_zihai[1],k_zihai[2])
        final_array += kzihaiOfvector
    return final_array

#test
print(len(yakudoraOfzihai_convert(hand,bakaze,jikaze,dora)))

#1つ下のabs_count_dora_convertのsub関数
def cmbinate_bctor2(k,l,m):
    # サイズ３の配列[4,4,1]
    size_array = [5, 5, 2]
    # (k, l, m)の組み合わせの総数
    total_combinations = np.prod(size_array)
    # 新しいサイズ50の初期値がすべて0の配列を作成
    output_array = [0] * 50
    # (k, l, m)の組み合わせに対応するインデックスに1を設定
    for a in range(size_array[0]):
        for b in range(size_array[1]):
            for c in range(size_array[2]):
                if a == k and b == l and c == m:
                    index = a * size_array[1] * size_array[2] + l * size_array[2] + m
                    output_array[index] = 1
                    #print(index)
    return output_array



#数牌の数字-5 の絶対値と枚数とドラの組合せ変換
#これ特徴量5*5*2とあるが、３色９種類の3*9*(5*5*2) = 1350で行う。
def abs_count_dora_convert(hand,dora):
    comb_result = calculate_kazuhai_feature.calculate_kazuhai_feature(hand,dora)
    #いまcomb_resultは[[mの数-5],[pの数-5],[sの数-5],[mの枚数],,,]になっているため、色ごとに分離
    manzu_feature450 = [[],[],[]]
    pinzu_feature450 = [[],[],[]]
    souzu_feature450 = [[],[],[]]
    #各色の特徴量を抽出して分離
    for k_col in range(len(comb_result)):
        for k_hai in range(len(comb_result[k_col])):
            if k_col == 0: #数牌-5のabs
                if k_hai == 0:
                    manzu_feature450[0] = comb_result[0][0]
                elif k_hai == 1:
                    pinzu_feature450[0] = comb_result[0][1]
                else:
                    souzu_feature450[0] = comb_result[0][2]
            if k_col == 1: #枚数情報
                if k_hai == 0:
                    manzu_feature450[1] = comb_result[1][0]
                elif k_hai == 1:
                    pinzu_feature450[1] = comb_result[1][1]
                else:
                    souzu_feature450[1] = comb_result[1][2]
            else: #ドラ情報
                if k_hai == 0:
                    manzu_feature450[2] = comb_result[2][0]
                elif k_hai == 1:
                    pinzu_feature450[2] = comb_result[2][1]
                else:
                    souzu_feature450[2] = comb_result[2][2]  
    #print(comb_result)
    #print(manzu_feature450) 
    #print(pinzu_feature450)
    #print(souzu_feature450)
    def k_col_convert_sub(k_col_feature450):
        result_array = []
        for column_values in zip(*k_col_feature450):
            result_array.append(list(column_values))
        #ex.)print(result_array) = [[4, 2, 0], [3, 0, 0], [2, 0, 0], [1, 1, 0], [0, 0, 0], [1, 0, 0], [2, 1, 0], [3, 0, 0], [4, 0, 0]]
        return result_array
    middle_form_manzu = k_col_convert_sub(manzu_feature450)
    middle_form_pinzu = k_col_convert_sub(pinzu_feature450)
    middle_form_souzu = k_col_convert_sub(souzu_feature450)
    #print(middle_form_manzu)
    #print(middle_form_pinzu)
    final_array = []
    for k_m in middle_form_manzu:
        k_mOfvector = cmbinate_bctor2(k_m[0],k_m[1],k_m[2])
        final_array += k_mOfvector
    #print(final_array)
    for k_p in middle_form_pinzu:
        k_pOfvector = cmbinate_bctor2(k_p[0],k_p[1],k_p[2])
        final_array += k_pOfvector
    for k_s in middle_form_souzu:
        k_sOfvector = cmbinate_bctor2(k_s[0],k_s[1],k_s[2])
        final_array += k_sOfvector
    return final_array
#test
#print(abs_count_dora_convert(hand,dora))
print(len(abs_count_dora_convert(hand,dora)))


#各色1~9の有無
#これ特徴量512(=2^9)とあるが、各職に対して3*2^9行う。
def isExi_convert(hand):
    isExi_result = calculate_1to9_feature.calculate_1to9_feature(hand)
    final_array = []
    for k_col in range(len(isExi_result)):
        index = 0
        k_array = [0] * 2**9
        #ex.) isExi_result[k_col] -> [1,1,0,0,0,1,0,0,0]
        for i in range(len(isExi_result[k_col])): 
            index +=  isExi_result[k_col][i] * 2 ** (i) #index０から。[1,1,0,0,0,0,0,0,0]は2^0+2^1=3番目    
        k_array[index] = 1    #用意した512サイズの配列のうちindex番目を点灯
        final_array += k_array
        
        #ex.) マンズの有無が[1,0,0,1,0,0,1,0,0] -> print(index) = 73
        #print(isExi_result[k_col])
        #print("index:" ,index)
        #print(k_array)
    return final_array
#test
print(len(isExi_convert(hand)))

def continuous_convert(hand):
    return calculate_continuous_feature.calculate_continuous_feature(hand)
#test
print(len(continuous_convert(hand)))

def tanyao_convert(hand):
    mahjong_hand = convert_haicode.convert_array_to_string(hand)
    normal_result = calculate_tanyao_xiangting.xiangting(calculate_tanyao_xiangting.shoupai(mahjong_hand))
    normal_dataset = [0] * 10
    normal_dataset[normal_result + 1] = 1 #range-1~8よりインデックスをインクリメント
    return normal_dataset
print(len(tanyao_convert(hand)))

#全特徴量ベクトルの結合
def append_all_dataset(hand,bakaze,jikaze,dora):
    all_dataset = normal_convert(hand) + titoi_convert(hand) + kokusi_convert(hand) + erase_one_convert(hand) + erase_two_convert(hand) + erase_three_convert(hand) + maxcolors_convert(hand) + sumOfColandZihai_convert(hand) + countOf2To8_convert(hand) + mentucomb_convert(hand) + yakudoraOfzihai_convert(hand,bakaze,jikaze,dora) + abs_count_dora_convert(hand,dora) + isExi_convert(hand) + continuous_convert(hand) + tanyao_convert(hand)
    return all_dataset

print(append_all_dataset(hand,bakaze,jikaze,dora))
print(len(append_all_dataset(hand,bakaze,jikaze,dora)))