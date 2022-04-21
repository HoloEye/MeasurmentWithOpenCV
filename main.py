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
        
        imgContours2, finalContours2 = functions.getContours(imgWarp,cThreshold = [50, 50],showCanny=False, minArea=2000,filter=4,draw=False)

    #
    #
        if len(finalContours) !=0:
            for obj in finalContours2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
                nPoints = functions.reorder((obj[2]))
                mW = round((functions.findDistance(nPoints[0][0] // scale,nPoints[1][0]//scale)/10),1)
                hW = round((functions.findDistance(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10), 1)

                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]), (255, 0, 0), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]), (255, 0, 0), 3, 8, 0, 0.05)

                x,y,w,h = obj[3]
                cv2.putText(imgContours2,'{}cm'.format(mW),(x+10,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(255,0, 0),None)
                cv2.putText(imgContours2, '{}cm'.format(hW), (x - 70, y + h//2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 0), None)
        cv2.imshow("Measured", imgContours2)

    cv2.imshow("Original", imgContours)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

    cv2.waitKey(1)