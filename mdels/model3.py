#under-sampling over-sampling
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
#imbalanced-learnの使用

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

#under-sampling
positive_count_train = train_label.sum()
rus = RandomUnderSampler(sampling_strategy={0:positive_count_train*9, 1:positive_count_train}, random_state=0)
#sampling_strategyはdefaultだと少数派のみresamplingするようになってる(←でもいいかも)
#古い情報だとsampling_strategyがratioになってたりするらしい
train_data_u, train_label_u = rus.fit_sample(train_data, train_label)

#over-sampling
ros = RandomOverSampler(random_state=0)#sampling_strategyの設定さぼってる
train_data_o, train_label_u = ros.fit_sample(train_data, train_label)
#https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html


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
    #*↑で作ったresampledデータを入れる
    epochs = 1000,
    batch_size = 1024,
    validation_data = (validation_data, validation_label),
    callbacks = [keras.callbacks.EarlyStopping(monitor='val_auc_1', patience=3, mode='max')]
    #EarlyStoppingはval_auc_1=PR-AUCをmonitor


#参考
#https://qiita.com/F8LUUI5kOxLvrmuIAIPwFsUWSKNdgW5N/items/99af44e253201b5b2dc2
#https://ohke.hateblo.jp/entry/2017/08/18/230000

#SMOTEはもっと調べないと使えない