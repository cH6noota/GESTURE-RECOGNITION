#パラメーター:{'C': 1e-05, 'decision_function_shape': 'ovr', 'kernel': 'linear', 'random_state': 42}
#ベストスコア: 1.0
import glob
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_gaussian_quantiles
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.externals import joblib

# データの生成
X=np.load("X_test.npy").reshape(5429,28*4)
y=np.load ("y_test.npy")
train_X, test_X, train_y, test_y = train_test_split(
    X, y, test_size=0.3, random_state=42)

# 以下にコードを記述してください
# モデルの構築
model = SVC(C=1e-05, decision_function_shape='ovr',kernel='linear',random_state= 42)

# train_Xとtrain_yを使ってモデルに学習させる
model.fit(train_X, train_y)

# 予測モデルをシリアライズ
#joblib.dump(model, 'svc.pkl') 

# 正解率の算出
print("線形SVM-score: {}".format(model.score(test_X, test_y)))

list1=glob.glob("/Users/moritachikara/Desktop/testdata/*.npy")

for j,name in enumerate(list1):
        test=np.load(name).reshape(1,28*4)
        Y_pred = model.predict(test)
        print(Y_pred)


