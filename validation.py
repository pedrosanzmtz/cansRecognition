from __future__ import print_function, division, absolute_import
from glob import glob
from keras.models import model_from_json
import cv2
import numpy as np

def get_model():
	json_file = open('model_color.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	loaded_model.load_weights('model_color.h5')
	return loaded_model

if __name__ == '__main__':
	folder = 'validation/'
	ext = '.jpg'
	query = folder + '*' + ext
	model = get_model()
	for file in glob(query):
		img = cv2.imread(file)
		img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
		img = img.reshape(1, 3, 32, 32)
		img = img / 255.0
		img = img.astype('float32')
		result = model.predict(img)
		print(file, result)