import numpy as np

class AveragedPerceptron:
    def __init__(self, num_features=136):
        self.weights = np.zeros(num_features)
        self.total_weights = np.zeros(num_features)
        self.counter = 0

    def predict(self, features):
        # 各特徴ベクトルに対するスコアを計算
        scores = np.dot(features, self.weights)
        # 最も高いスコアのアクションを選択
        return np.argmax(scores)

    def update_weights(self, chosen_features, correct_features):
        # 選択されたアクションが正しくない場合は重みを更新
        if not np.array_equal(chosen_features, correct_features):
            self.weights += correct_features - chosen_features
        # 平均のためのカウンターと総重みを更新
        self.counter += 1
        self.total_weights += self.weights

    def finalize_weights(self):
        # 更新があった場合に平均化された重みを最終化
        if self.counter > 0:
            return self.total_weights / self.counter
        else:
            return self.weights  # 更新がなければ、元の重みを返す

# 使用例:
# 特徴ベクトルとそれに対応する正しい特徴ベクトルがあると仮定
# features = [feature_vector1, feature_vector2, ...]
# correct_features = [correct_feature_vector1, correct_feature_vector2, ...]

perceptron = AveragedPerceptron(num_features=136)

# パーセプトロンを訓練
for feature_vector, correct_feature_vector in zip(features, correct_features):
    chosen_action = perceptron.predict(feature_vector)
    chosen_features = feature_vector[chosen_action]  # これが選ばれた特徴を得る方法だと仮定
    perceptron.update_weights(chosen_features, correct_feature_vector)

# 訓練が終了した後
average_weights = perceptron.finalize_weights()
