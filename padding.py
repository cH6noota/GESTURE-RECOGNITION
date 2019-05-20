import numpy as np
import glob
inp="tokei_mawashi"
DIR="./raw/"+inp
DIR2="./padding/"+inp+"_p/"
list1=glob.glob(DIR+"/*.npy")
list2=glob.glob(DIR+"_water/*.npy")
for j,name in enumerate(list1):
	X=np.load( name )
	x = np.zeros([28, 4], dtype=np.int32)
	for i, xi in enumerate(X):
		x[i, :len(xi)] = xi[:]
	np.save(DIR2+str(j+1)+".npy",x)
for k,name in enumerate(list2):
        X=np.load( name )
        x = np.zeros([28, 4], dtype=np.int32)
        for i, xi in enumerate(X):
                x[i, :len(xi)] = xi[:]
        np.save("./padding/"+inp+"_water_p/"+str(k+1)+".npy" ,x)
