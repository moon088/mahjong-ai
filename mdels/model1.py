import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
from sklearn.model_selection import train_test_split

filepath1 = ''#FIXME: path
filepath2 = ''#FIXME: path
#! path入れて

f1 = open(filepath1, 'rb')
f2 = open(filepath2, 'rb')

mj_data = pickle.load(f1)#特徴量ベクトル
mj_target = pickle.load(f2)#ラベルベクトル
#別にpickleでなくてもいい
train_data, validation_data, train_label, validation_label = train_test_split(
    mj_data,
    mj_target,
    test_size = 0.2
)

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
        keras.metrics.AUC(curve='PR'),#TODO: args
        #PR-AUCによる評価
        #閾値の設定に謎がある
        keras.metrics.Precision(),
        keras.metrics.Recall()
    ]
)

print(model.summary())

history = model.fit(
    x = train_data,
    y = train_label,
    epochs = 1000,
    batch_size = 1024,
    validation_data = (validation_data, validation_label),
    callbacks = [keras.callbacks.EarlyStopping(monitor='val_auc_1', patience=3, mode='max')]
    #EarlyStoppingのmonitor変更する可能性あり val_auc_1とかに (default: val_acc)
    #* ↑変更済み
    #aucならmode=max
)


#おおよそはこんな感じ
#各種設定値はあまり自信ない 初めて使ってるものが結構あるので
#metricsと,EarlyStoppingの引数あたりが特にあやしい
#keras.datasets.imdbで動作を見たところ、動きはする
#*不均衡データ使ってテストしたい credit card fraud detectionとか
#*やっぱりEarlyStoppingにはPR-AUCをmonitorしてもらった方がいいかも