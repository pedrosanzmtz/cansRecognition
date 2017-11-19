import cv2
import numpy as np
from keras.models import model_from_json
from validation import get_model

model = get_model()

values = ['pepsi', 'manzanita', '7up']

def predict(data):
	img = np.fromstring(data, np.uint8)
	img = cv2.imdecode(img, cv2.IMREAD_COLOR)
	#print(img.shape)
	img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
	img = img.reshape(1, 3, 32, 32)
	img = img / 255.0
	img = img.astype('float32')
	r = model.predict(img)
	result = dict()
	result['pepsi'] = round(r[0][0], 4)
	result['manzanita'] = round(r[0][1], 4)
	result['7up'] = round(r[0][2], 4)
	return result