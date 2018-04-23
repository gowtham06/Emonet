#!/N/u/gkbandep/BigRed2/.conda_envs/vision/bin/python
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
from keras.layers import BatchNormalization
from PIL import ImageFile
import numpy as np
ImageFile.LOAD_TRUNCATED_IMAGES = True
img_width, img_height = 224,224
sess = K.get_session()
def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(img_width, img_height))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = img_tensor.reshape(1,3, img_width, img_height)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    # if show:
    #     plt.imshow(img_tensor[0])                           
    #     plt.axis('off')
    #     plt.show()

    return img_tensor

def predict_class(modelFile):
	model = load_model(modelFile)
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	labels=['NONE','UNCERTAIN','SAD','NEUTRAL','DISGUST','ANGER','SURPRISE','FEAR', 'NO_FACE','CONTEMPT','HAPPY']
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

	# train_data_dir = 'Data/TRAIN'
	# validation_data_dir = 'Data/validation'
	# train_datagen = ImageDataGenerator(rescale=1. / 255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
	# train_generator = train_datagen.flow_from_directory(train_data_dir,target_size=(img_width, img_height),batch_size=50,class_mode='categorical')
	# class_dictionary=train_generator.class_indices
	# print(class_dictionary)

if __name__ == '__main__':
	modelFile='Classifier.h5'
	predict_class(modelFile)