import numpy as np
from Param.params import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Input, Flatten, Reshape, Dropout, MaxPool2D
from tensorflow.keras import Input

class Model():
    def __init__(self):
        pass
    
    # 3 pixel model
    def build_model(self, output_activation="softmax", loss="categorical_crossentropy", optimizer="adam"):
        input_size = [n_pixels*(window+2), n_pixels*4, 3]
        #input_size = [n_pixels*window, n_pixels*2, 3]

        model = Sequential()
        model.add(Input(shape = (1, input_size[0]*input_size[1]*input_size[2])))
        model.add(Reshape(target_shape=[-1, input_size[0], input_size[1], input_size[2]]))

        # Conv blocks
        model.add(Conv2D(32, kernel_size=(9, 9), strides=(3, 3), activation="relu", padding="same"))
        model.add(Conv2D(64, kernel_size=(6, 6), strides=(3, 3), activation="relu", padding="same"))
        model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), activation="relu", padding="same"))
        model.add(Conv2D(512, kernel_size=(int(np.ceil((window+2)/3)), 2), strides=(1, 1), activation="relu", padding="valid"))

        # Dense blocks
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(n_actions, activation=output_activation))   # Output softmax layer

        model.compile(
            loss = loss,
            optimizer = optimizer,
            metrics = ["accuracy"])
        return model

    # AutoKeras model architecture (2 pixel)
    def build_autokeras_model(self, output_activation="softmax", loss="categorical_crossentropy", optimizer="adam"):
        #input_size = [n_pixels*(window+2), n_pixels*4, 3]
        input_size = [n_pixels*window, n_pixels*2, 3]

        model = Sequential()
        model.add(Input(shape = (1, input_size[0]*input_size[1]*input_size[2])))
        model.add(Reshape(target_shape=[input_size[0], input_size[1], input_size[2]]))

        # # Conv blocks
        model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), activation="relu", padding="same"))
        model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), activation="relu", padding="same"))
        model.add(MaxPool2D())
        model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), activation="relu", padding="same"))
        model.add(Conv2D(32, kernel_size=(3, 3), strides=(1, 1), activation="relu", padding="same"))
        model.add(MaxPool2D(padding="same"))

        # Dense blocks
        model.add(Flatten())
        #model.add(Dropout(0.3))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(n_actions, activation=output_activation))   # Output softmax layer

        model.compile(
            loss = loss,
            optimizer = optimizer,
            metrics = ["accuracy"])
        return model