'''import cv2
from cv2 import imread
from random import randrange
trained_face_data=cv2.CascadeClassifier('haarcascade_frontal_face_detector.xml')
img=imread('devbaba.jpeg')
gray_scale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinates=trained_face_data.detectMultiScale(gray_scale_img)
#print(face_coordinates)
for(x,y,w,h) in face_coordinates:
 #   cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
    #cv2.rectangle(img(287 ,372),(33  ,33),(0,225,0),2)
    #cv2.rectangle(img,(452,209),(452+211,209+211),(0,255,0),2)
#(x,y,w,h)=face_coordinates[0]
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(225),randrange(256),10))


cv2.imshow('cleverprogrammer',img)
cv2.waitKey()
'''

import cv2
from cv2 import imread
from random import randrange
trained_face_data=cv2.CascadeClassifier('haarcascade_frontal_face_detector.xml')
webcam=cv2.VideoCapture(0)
while True:
    successful_frame_read, frame=webcam.read()
    gray_scale_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(gray_scale_img)
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(226),randrange(256),10))
        

    cv2.imshow('cleverprogrammer',frame)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
'''face_coordinates=trained_face_data.detectMultiScale(gray_scale_img)
#print(face_coordinates)
for(x,y,w,h) in face_coordinates:
 #   cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
    #cv2.rectangle(img(287 ,372),(33  ,33),(0,225,0),2)
    #cv2.rectangle(img,(452,209),(452+211,209+211),(0,255,0),2)
#(x,y,w,h)=face_coordinates[0]
    cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(225),randrange(256),10))
'''
#cv2.imshow('cleverprogrammer',gray_scale_img)
#cv2.waitKey()