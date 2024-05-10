# これは牌の次元と、七対子だけ対応させた特徴量ベクトル生成のコード



def create_feature_vector(indices_136):
    """
    牌の次元と、七対子だけ対応させた特徴量ベクトルを生成する関数。
    136次元のベクトルと7要素のベクトルを作成し、指定されたインデックスを1に更新して結合する。
    
    :param indices_136: 136次元ベクトルで1に更新するインデックスのリスト
    :param variable_index: 7要素ベクトルで1に更新するインデックス
    :return: 結合された特徴量ベクトル
    """
    # 136次元のベクトルを作成し、全ての要素を0で初期化
    vector_136 = [0] * 136
    
    # リストに含まれるインデックスの要素を1に更新（136次元ベクトル用）
    for index in indices_136:
        if 0 <= index < len(vector_136):  # インデックスがベクトルの範囲内にあることを確認
            vector_136[index] = 1
    
    # 7要素のリストを作成し、全ての要素を0で初期化
    # vector_7 = [0] * 7
    
    # 変数の値と同じ位置の要素を1に更新（7要素ベクトル用）
    # if 0 <= variable_index < len(vector_7):  # インデックスがベクトルの範囲内にあることを確認
        #vector_7[variable_index] = 1
    
    # 136次元ベクトルと7要素ベクトルを結合
    # combined_vector = vector_136 + vector_7
    
    # 結果を返す
    # return combined_vector
    # 本当はcombined_vectorだけど、一旦136だけにしてる。
    return vector_136 

# 使用例:
if __name__ == "__main__":
    indices_136_example = [0, 4]
    #variable_index_example = 3
    print(create_feature_vector(indices_136_example))

