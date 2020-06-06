from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error 
from sklearn.metrics import accuracy_score


def model(input_size):
	
	mod=Sequential()

	mod.add(Dense(32, kernel_initializer='normal',input_dim = input_size, activation='relu'))


	mod.add(Dense(64, kernel_initializer='normal',activation='relu'))
	mod.add(Dense(128, kernel_initializer='normal',activation='relu'))
	mod.add(Dense(128, kernel_initializer='normal',activation='relu'))
	mod.add(Dense(256, kernel_initializer='normal',activation='relu'))

	mod.add(Dense(1, kernel_initializer='normal',activation='linear'))

	mod.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
	mod.summary()

	return mod