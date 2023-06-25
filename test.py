









import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
count = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)

    count=1

   
    if count>0:
        if len(contour)>=2:
            cv2.putText(img=frame, text='two hands detected indicates mouse click', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(255, 0, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print(str(x) +" "+str(y)+" if x > 500 right click will happen. if x < 500 left click will happen")
                if x > 500:
                   pyautogui.click(button='right')
                if x < 500:
                   pyautogui.click(x,y)		

        elif len(contour)==1:
            cv2.putText(img=frame, text='Single hand detected indicates mouse move', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if x > 0 and y > 0:
                  print(str(x) +" "+str(y))
                  pyautogui.moveTo(x,y)

        elif len(contour)==0:
            cv2.putText(img=frame, text='No hand detected', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))
                

    count+=1

    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()