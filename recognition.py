import cv2, urllib
import numpy as np
from keras.models import model_from_json
from validation import get_model

model = get_model()

def predict(data):
	img = np.fromstring(data, np.uint8)
	img = cv2.imdecode(img, cv2.IMREAD_COLOR)
	img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)
	img = img.reshape(1, 3, 32, 32)
	img = img / 255.0
	img = img.astype('float32')
	result = model.predict(img)
	return result