import numpy as np
  

def read(name):
        return np.load(name)
data1 = read("/Users/moritachikara/Desktop/motion_dataset/1/y1.npy")
data2 = read("/Users/moritachikara/Desktop/motion_dataset/2/y2.npy")
data3 = read("/Users/moritachikara/Desktop/motion_dataset/3/y3.npy")
data4 = read("/Users/moritachikara/Desktop/motion_dataset/4/y4.npy")
data0=  read("/Users/moritachikara/Desktop/motion_dataset/-1/y-1.npy")
marge=np.concatenate([data1, data2,data3,data4,data0])

np.save('./y_test.npy',marge)
