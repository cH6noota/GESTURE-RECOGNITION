import cv2
import time
import numpy as np
def padding(X,op) :
    x = np.zeros([28, 4], dtype=np.int32)
    for i, xi in enumerate(X):
        x[i, :len(xi)] = xi[:]
    np.save("./c_"+str(op)+".npy", x )
def means(data,new):
    data=data.reshape(1,4)
    re_val =  []
    for i in range (4):
        re_val.append( (data[0][i]+new[0][i])/2 ) 
    return np.array([re_val])   # 1*4 np_arrayで返す
yaruki=0
op=0
cap = cv2.VideoCapture(0)
Start=0
detect_d= np.empty((0,4))
before = None
while True:
    #  OpenCVでWebカメラの画像を取り込む
    ret, frame = cap.read()
    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)

    # 取り込んだフレームに対して差分をとって動いているところが明るい画像を作る
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if before is None:
        before = gray.copy().astype('float')
        continue
    # 現フレームと前フレームの加重平均を使うと良いらしい
    cv2.accumulateWeighted(gray, before, 0.5)
    mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))
    # 動いているところが明るい画像を表示する
    cv2.imshow('MotionDetected Frame', mdframe)

    # 動いているエリアの面積を計算してちょうどいい検出結果を抽出する
    thresh = cv2.threshold(mdframe, 3, 255, cv2.THRESH_BINARY)[1]
    # 輪郭データに変換しくれるfindContours
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    target = contours[0]
    for cnt in contours:
         #輪郭の面積を求めてくれるcontourArea
        area = cv2.contourArea(cnt)
        #一番大きいエリアを取得(1000<エリア<10000)
        if max_area < area and area < 50000 and area > 10000:
            max_area = area
            target = cnt

    # 動いているエリアのうちそこそこの大きさのものがあればそれを矩形で表示する
    if max_area <= 1000:
        if Start== 0 :
            Start=0
            areaframe = frame
            cv2.putText(areaframe, 'not detected', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
        elif Start==-2:
            if len(detect_d)>10:
               op=op+1
               padding(detect_d ,op)
               print(str(op)+"データを保存しました-->"+str(detect_d.shape))
               time.sleep(3)
            detect_d=np.empty((0,4))
            Start=0
            print("データリセット")
            areaframe = frame
            cv2.putText(areaframe, 'reset', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
            time.sleep(2)
        elif Start==-1 :
            Start=-2
            areaframe = frame
            cv2.putText(areaframe, 'kesson2', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)
        elif Start==1:
            Start=-1
            areaframe = frame
            cv2.putText(areaframe, 'kesson1', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)



    else:
        x,y,w,h = cv2.boundingRect(target)
        new=np.array([ [x,y,w,h] ])
        if Start==-2:
           #欠損値の処理
           last_index=detect_d.shape[0]-1
           mid = means(detect_d[last_index],new)
           mid_s = means(detect_d[last_index] , mid )
           mid_l = means(mid ,new)
           detect_d=np.append(detect_d, mid_s , axis=0)
           detect_d=np.append(detect_d, mid_l , axis=0)
        elif Start== -1:
           #欠損値の処理
           last_index=detect_d.shape[0]-1
           detect_d=np.append(detect_d ,means(detect_d[last_index],new),axis=0)
        if len(detect_d) > 27:
           detect_d = np.empty((0,4))
           print("長さすぎますよ")
           time.sleep(2)
        detect_d=np.append(detect_d,new, axis=0)
        Start=1
        print(x)
        print(y)
        print(w)
        print(h)
        print("---------------")
        # 諸般の事情で矩形検出とした。
        areaframe = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('MotionDetected Area Frame', areaframe)
    time.sleep(0.1)
    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()
