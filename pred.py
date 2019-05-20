import numpy as np
from sklearn import datasets
from sklearn.externals import joblib
import glob

# 予測モデルを復元
model = joblib.load('svc.pkl')

list1=glob.glob("/Users/moritachikara/Desktop/testdata/*.npy")

for j,name in enumerate(list1):
        test=np.load(name).reshape(1,28*4)
        Y_pred = model.predict(test)
        print(Y_pred)

