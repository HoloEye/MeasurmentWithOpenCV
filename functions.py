import cv2
import numpy as np

def getContours(img,cThreshold = [100, 100],showCanny = False, minArea = 1000, filter = 0,draw = False):
    imgGRay = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGRay,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,cThreshold[0],cThreshold[1])
    kernel = np.ones((5,5))
    imgDilatation = cv2.dilate(imgCanny,kernel,iterations=3)
    imgErosion = cv2.erode(imgDilatation,kernel,iterations=2)
    if showCanny:cv2.imshow('Prepared image',imgErosion)

    contours, chierarchy = cv2.findContours(imgErosion,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > minArea:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            bbox = cv2.boundingRect(approx)
            if filter > 0:
                if len(approx) == filter:
                    finalContours.append([len(approx),area,approx,bbox,i])
            else:
                 finalContours.append([len(approx),area,approx,bbox,i])

    finalContours = sorted(finalContours, key = lambda x:x[1], reverse = True )
    if draw:
        for con in finalContours:
            cv2.drawContours(img,con[4],-1,(0,0,255),3)

    return img, finalContours
