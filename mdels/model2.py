#学習アルゴリズムを変更
#パラメータ更新に重み付け
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
from sklearn.model_selection import train_test_split

filepath1 = ''#FIXME: path
filepath2 = ''#FIXME: path
#! path入れて


mj_data = pickle.load(filepath1)#特徴量ベクトル
mj_target = pickle.load(filepath2)#ラベルベクトル
#別にpickleでなくてもいい
train_data, validation_data, train_label, validation_label = train_test_split(
    mj_data,
    mj_target,
    test_size = 0.2
)

#学習時にクラス重みを調整するための重み計算
def get_class_weights(num_of_class_samples, beta=0.99):
    num_of_class = len(num_of_class_samples)
    effective_num = 1.0 - np.power(beta, num_of_class_samples)
    weights = (1.0 - beta) / effective_num
    weights = weights / np.sum(weights) * num_of_class
    return weights
#データから計算する関数
#事前にラベルの0,1の個数を数える必要あり
#weights = get_class_weights([])
class_weight = {
    0: 1.0,
    1: 13.0
}
#https://qiita.com/sintome0409/questions/e39b000b86cc06e4dae2
#https://qastack.jp/datascience/13490/how-to-set-class-weights-for-imbalanced-classes-in-keras

model = keras.Sequential(
    [
        keras.layers.Dense(32, activation='relu', input_shape=(37514,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
        #必要に応じてDropoutの追加
    ]
)

model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = [
        'accuracy',
        #普通の精度評価 あまり当てにならない
        keras.metrics.F1Score(average='weighted', threshold=0.5),#TODO: args
        #F1値による評価
        keras.metrics.AUC(curve='PR')#TODO: args
        #PR-AUCによる評価
    ]
)

print(model.summary())

history = model.fit(
    x = train_data,
    y = train_label,
    class_weight = class_weight,
    #クラスの重みの設定
    #https://www.tensorflow.org/guide/keras/train_and_evaluate?hl=ja
    #https://keras.io/api/models/model_training_apis/
    epochs = 1000,
    batch_size = 1024,
    validation_data = (validation_data, validation_label),
    callbacks = [keras.callbacks.EarlyStopping(monitor='val_auc_1', patience=3, mode='max')]
    #EarlyStoppingはval_auc_1=PR-AUCをmonitor
)

#基本方針は↓のような感じ
#https://qiita.com/dcm_yukimasa-kaneda/items/5eaadbdeec10d92020c6