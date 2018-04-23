#!/Users/gowthamkannan/anaconda3/bin/python
import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv.imread('_738.jpeg')
img_2=cv.imread('_752.jpg')
img_3=cv.imread('_262.jpg')
print(img.shape,img_2.shape,img_3.shape)
# rows,cols,height=img_2.shape
img = cv.resize(img, (img_2.shape[0],img_2.shape[1])) 
# img = cv.resize(img, img_2.shape) 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv.imwrite('face_detect.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()