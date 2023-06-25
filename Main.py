









import imutils
import time
import cv2
import pyautogui

webcamera = cv2.VideoCapture(0)
time.sleep(0.25)

oldFrame = None

while True:
    (grab, frame) = webcamera.read()
    
    if not grab:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if oldFrame is None:
        oldFrame = gray
        continue

    frameDelta = cv2.absdiff(oldFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
      if cv2.contourArea(c) < 500:
         continue
      (x, y, w, h) = cv2.boundingRect(c)
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      
      if x > 0 and y > 0:
         pyautogui.moveTo(x,y)
         print(str(x) +" "+str(y))

    
    cv2.imshow("Virtual Mouse Movement", frame)
    key = cv2.waitKey(1) &  0xFF

    if key == ord("q"):
        break

webcamera.release()
cv2.destroyAllWindows()