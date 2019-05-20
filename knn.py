import pandas as pd
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.neighbors import KNeighborsClassifier
import glob
X=np.load("X_test.npy").reshape(6597,28*4)
y=np.load ("y_test.npy")
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state=3) 


# モデルの構築
model = KNeighborsClassifier( n_neighbors=1)

# モデルの学習
model.fit(train_X, train_y)

# 正解率の表示
print(model.score(test_X, test_y))

list1=glob.glob("/Users/moritachikara/Desktop/testdata/*.npy")

for j,name in enumerate(list1):
	test=np.load(name).reshape(1,28*4)
	Y_pred = model.predict(test) 
	print(Y_pred)


