#モデルの詳細なコード
#実行はできないよ
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

sys.path.append('/content/drive/MyDrive/実験2/prj-14')

filepath1 = '/content/drive/MyDrive/実験2/prj-14/mj_files/data200.pkl'#FIXME: path
filepath2 = '/content/drive/MyDrive/実験2/prj-14/mj_files/label200.pkl'#FIXME: path
#! path入れて

f1 = open(filepath1, 'rb')
f2 = open(filepath2, 'rb')

mj_data = pickle.load(f1)#特徴量ベクトル
mj_target = pickle.load(f2)#ラベルベクトル
train_data, validation_data, train_label, validation_label = train_test_split(
    mj_data,
    mj_target,
    test_size = 0.2
)

#モデル定義
model1 = keras.Sequential(
    [
        keras.layers.Dense(64, activation='relu', input_shape=(3209,)),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(1, activation='sigmoid')
    ]
)

model1.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = [
        'accuracy',
        #普通の精度評価 あまり当てにならない
        keras.metrics.F1Score(average='weighted', threshold=0.5),
        #F1値による評価
        keras.metrics.AUC(curve='PR', name='auc1'),
        #PR-AUCによる評価
        keras.metrics.Precision(name='pre1'),
        keras.metrics.Recall(name='rec1')
    ]
)

print(model1.summary())


#学習
#パラメータ更新の重み
class_weight = {
    0: 1.0,
    1: 5.0
}

history1 = model1.fit(
    x = train_data,
    y = train_label,
    class_weight = class_weight,
    epochs = 100,
    batch_size = 2048,
    validation_data = (validation_data, validation_label),
    callbacks = [
        keras.callbacks.EarlyStopping(monitor='val_auc1', patience=3, mode='max'),
        keras.callbacks.EarlyStopping(monitor='val_pre1', patience=3, mode='max')
    ]
)


#評価
history_dict = history1.history
print(history_dict.keys())

loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc = history_dict['accuracy']
f1_values = history_dict['f1_score']
val_f1_values = history_dict['val_f1_score']
auc_values = history_dict['auc1']
val_auc_values = history_dict['val_auc1']
pre_values = history_dict['pre1']
val_pre_values = history_dict['val_pre1']
rec_values = history_dict['rec1']
val_rec_values = history_dict['val_rec1']


epochs = range(1, len(acc) + 1)

plt.plot(epochs, f1_values, 'bo', label='Training f1')
plt.plot(epochs, val_f1_values, 'b', label='Validation f1')
plt.title('Training and validation f1 score')
plt.xlabel('Epochs')
plt.ylabel('F1 Score')
plt.legend()

plt.show()

val_acc_values = history_dict['val_accuracy']

plt.plot(epochs, auc_values, 'bo', label='Training auc')
plt.plot(epochs, val_auc_values, 'b', label='Validation auc')
plt.title('Training and validation auc')
plt.xlabel('Epochs')
plt.ylabel('PR-AUC')
plt.legend()

plt.show()

plt.plot(epochs, acc, 'bo', label='Training Accuracy')
plt.plot(epochs, val_acc_values, 'b', label='Validation Accuracy')
plt.title('Training and validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

plt.plot(epochs, loss_values, 'bo', label='Training Loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.plot(epochs, pre_values, 'bo', label='Training Precision')
plt.plot(epochs, val_pre_values, 'b', label='Validation Precision')
plt.title('Training and validation Precision')
plt.xlabel('Epochs')
plt.ylabel('Precision')
plt.legend()

plt.show()

plt.plot(epochs, rec_values, 'bo', label='Training Recall')
plt.plot(epochs, val_rec_values, 'b', label='Validation Recall')
plt.title('Training and validation Recall')
plt.xlabel('Epochs')
plt.ylabel('Recall')
plt.legend()

plt.show()


model1.save('/content/drive/MyDrive/実験2/prj-14/models/my_model')