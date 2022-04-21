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

