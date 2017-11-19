from __future__ import print_function, division, absolute_import
import cv2
import numpy as np
from glob import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.externals import joblib


if __name__ == '__main__':
	folder = 'videos/'
	ext = '.mp4'
	query = folder + '*' + ext
	y = list()
	x = list()
	cont = 0
	for i, file in enumerate(glob(query)):
		name = file.strip(folder).strip(ext)
		cap = cv2.VideoCapture(file)
		while(cap.isOpened()):
			if cont % 100 == 0:
				print(cont, i)
			try:
				ret, frame = cap.read()
				frame = cv2.resize(frame, (32, 32), interpolation=cv2.INTER_AREA)
				x.append(frame)
				y.append(i)
				cont += 1
			except:
				break
		cap.release()

	label_binarizer = LabelBinarizer()
	label_binarizer.fit(y)
	X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
	joblib.dump(X_train, 'X_train.pkl') 
	joblib.dump(y_train, 'y_train.pkl') 
	joblib.dump(X_test, 'X_test.pkl') 
	joblib.dump(y_test, 'y_test.pkl') 