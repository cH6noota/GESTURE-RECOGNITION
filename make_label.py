import numpy as np
import glob
LABEL=4
DIR="./4/tokei_mawashi_p/*"
DIR2="./4/tokei_mawashi_p/*"

list1= glob.glob(DIR)
list2= glob.glob(DIR2)

flag=True
for index,item in enumerate(list1): 
	data=np.load(item).reshape(1,28,4)
	if flag is True:
		marge=data
		flag =False
	else :
		marge=np.concatenate([marge, data])

for index2,item in enumerate(list2):
        data=np.load(item).reshape(1,28,4)
        if flag is True:
                marge=data
                flag =False
        else :
                marge=np.concatenate([marge, data])


np.save("./4/X4.npy", marge)
y=np.full( (index+index2+2 ,1) , LABEL)
np.save("./"+str(LABEL)+"/y"+str(LABEL)+".npy",y)
