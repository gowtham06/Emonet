#!/Users/gowthamkannan/anaconda3/bin/python
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.models import Sequential
from keras.models import Input
from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense,concatenate
from keras import backend as K
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import keras.utils.np_utils as KUtils
from keras.layers import BatchNormalization
from PIL import ImageFile
import numpy as np
import sys,os
import cv2 as cv2
from inference import *
from preprocessor import *
from confusion_matrix import plot_mat
ImageFile.LOAD_TRUNCATED_IMAGES = True
img_width, img_height = 300,300
sess = K.get_session()
emotion_model_path = '/Users/gowthamkannan/CV_PROJ/TrainedModels/Classifier_500.h5'
emotion_classifier = load_model(emotion_model_path)
emotion_classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
def predict_class(image_path):
	emotion_labels=['NONE','UNCERTAIN','SAD','NEUTRAL','DISGUST','ANGER','SURPRISE','FEAR','CONTEMPT','HAPPY']
	emotion_labels=sorted(emotion_labels)
	bgr_image=cv2.imread(image_path)
	gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
	gray_image = cv2.resize(gray_image, (300,300))
	gray_image = preprocess_input(gray_image, True)
	gray_image = np.expand_dims(gray_image, -1)
	gray_image=np.resize(gray_image,(1,300,300,3))
	emotion_prediction = emotion_classifier.predict(gray_image)
	emotion_probability = np.max(emotion_prediction)
	emotion_label_arg = emotion_prediction.argmax()
	emotion_text = emotion_labels[emotion_label_arg]
	# print(emotion_text,emotion_probability)
	return emotion_text

def calulate_validation_score(validation_dir,categories):
	w, h = len(categories), len(categories);
	confusion_mat= [[0 for x in range(w)] for y in range(h)]
	for item in categories:
		folder_name=os.path.join(validation_dir,item)
		# print(folder_name)
		files=os.listdir(folder_name)
		for file in files:
			file_path=os.path.join(folder_name,file)
			# print(file_path)
			class_label=predict_class(file_path)
			print(item,class_label)
			confusion_mat[categories.index(item)][categories.index(class_label)]+=1

	print(confusion_mat)
	plot_mat(confusion_mat)




if __name__ == '__main__':
	validation_dir='/Users/gowthamkannan/CV_PROJ/VALIDAITON_DATA'
	categories=['ANGER','DISGUST','HAPPY','NONE','SAD','UNCERTAIN','CONTEMPT','FEAR','NEUTRAL','SURPRISE']
	categories=sorted(categories)
	calulate_validation_score(validation_dir,categories)
