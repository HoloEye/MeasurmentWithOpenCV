import  cv2 
import numpy as np
import  functions




webcam = False
path = 'test.jpg'
cap = cv2.VideoCapture(0)
cap.set(10,160 )
cap.set(3,1920)
cap.set(4, 1080)
scale = 3
wP =210*scale
hP = 297*scale


while True:
    if webcam:success, img = cap.read()
    else: img = cv2.imread(path)

    imgContours, finalContours =  functions.getContours(img,showCanny=False,minArea = 50000,filter=4,draw = False)



    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        
        imgWarp = functions.warpImg(img,biggest,wP, hP)
        cv2.imshow("A4", imgWarp)
           if cv2.waitKey(1) & 0xFF == ord('q'):
             break
