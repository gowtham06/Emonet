#!/N/u/gkbandep/BigRed2/.conda_envs/vision/bin/python
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.models import Sequential
from keras.models import Input
from keras.models import Model
from keras import backend as K
from keras.models import load_model
from keras.preprocessing import image
from PIL import ImageFile
import numpy as np
import cv2 as cv
ImageFile.LOAD_TRUNCATED_IMAGES = True
img_width, img_height = 224,224
sess = K.get_session()
import sys
def predict_class(modelFile):
	model = load_model(modelFile)
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	img_file='_10425.jpg'
	img_file='_1877966.jpg'

	# img = image.load_img(img_file, target_size=(img_width, img_height))
	# img=load_image(img_file)
	# x = image.img_to_array(img)
	# x = np.expand_dims(x, axis=0)
	# images = np.vstack([x])
	# classes = model.predict(img)
	# print(classes)
	img = tf.read_file(img_file)
	img = tf.image.decode_jpeg(img, channels=3)
	img.set_shape([None, None, 3])
	img = tf.image.resize_images(img, (img_width, img_height))
	img = img.eval(session=sess)
	img = np.expand_dims(img, 0)
	pred = model.predict(img)
	print(labels[np.argmax(pred)])

def faceDetctor():
	cascPath='haarcascade_frontalface_default.xml'
	faceCascade = cv2.CascadeClassifier(cascPath)
	video_capture = cv2.VideoCapture(0)
	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    # Our operations on the frame come here
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	    print(len(faces))
	    # Display the resulting frame
	    for (x,y,w,h) in faces:
	         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	         roi_gray = gray[y:y+h, x:x+w]
	         roi_color = frame[y:y+h, x:x+w]
	         eyes = eye_cascade.detectMultiScale(roi_gray)
	         for (ex,ey,ew,eh) in eyes:
	             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
if __name__ == '__main__':
	labels=['NONE','UNCERTAIN','SAD','NEUTRAL','DISGUST','ANGER','SURPRISE','FEAR', 'NO_FACE','CONTEMPT','HAPPY']
	modelFile='Classifier.h5'
	# predict_class(modelFile)
	