from numpy.random import *
import numpy as np
DIR="./raw/tokei_mawashi"

for j in range(10):
        X=np.load(DIR+"/c_"+str(j+1)+".npy")
        #右にずらし...x++
        for count in range(300):
                X_copy=X
                migi = randint(1,640)
                flag=True
                for i_d in range(len(X)):
                        if X_copy[i_d][0] + migi <=640 :
                                X_copy[i_d][0]=X[i_d][0]+migi
                        else:
                                flag=False
                if flag is True :
                        np.save(DIR+"_water/c_"+str(j+1)+"_xp"+str(migi)+".npy",X_copy)
        #左にずらし...x--
        for count in range(300):
                X_copy=X
                hidari = randint(1,640)
                flag=True
                for i_d in range(len(X)):
                        if X[i_d][0]-hidari>=0:
                                X_copy[i_d][0]=X[i_d][0]-hidari
                        else:
                                flag=False
                if flag is True :
                        np.save(DIR+"_water/c_"+str(j+1)+"_xm"+str(hidari)+".npy",X_copy)
        #上にずらし...y++
        for count in range(300):
                X_copy=X
                up = randint(1,480)
                flag=True
                for i_d in range(len(X)):
                        if X[i_d][1]+up<=480 :
                                X_copy[i_d][1]=X[i_d][1]+up
                        else:
                                flag=False
                if flag is True :
                        np.save(DIR+"_water/c_"+str(j+1)+"_yp"+str(up)+".npy",X_copy)
        #下にずらし ...y--
        for count in range(300):
                X_copy=X
                down = randint(1,480)
                flag=True
                for i_d in range(len(X)):
                        if X[i_d][1]-down>=0 :
                                X_copy[i_d][1]=X[i_d][1]-down
                        else:
                                flag=False
                if flag is True :
                        np.save(DIR+"_water/c_"+str(j+1)+"_ym"+str(down)+".npy",X_copy)
        #ランダムずらし
        for count in range(500):
                X_copy=X
                x= randint(1,640)
                y=randint(1,480)
                flag=True
                x_f= randint(0,2)
                y_f= randint(0,2)
                for i_d in range(len(X)):
                        if x_f == 1 and X[i_d][0]+x<=640 :
                                X_copy[i_d][0] =X[i_d][0]+x
                        elif x_f ==0 and X[i_d][0]-x>=0:
                                X_copy[i_d][0] =X[i_d][0]-x
                        else:
                                flag=False
                        if y_f ==1 and X[i_d][1]+y<=480:
                                X_copy[i_d][1]=X[i_d][1]+y
                        elif y_f ==0 and X[i_d][1]-y>=0:
                                X_copy[i_d][1]=X[i_d][1]-y
                        else :
                                flag=False
                if flag is True :
                        np.save(DIR+"_water/c_"+str(j+1)+"_random"+str(x+y)+".npy",X_copy)
