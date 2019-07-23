#import training and test data sets from keras
from keras.datasets import mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#imports to_categorical function from keras utilities
from keras.utils import to_categorical

#reclassifies and reshapes training and test data sets
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

#creates import layer using keras function
from keras.layers import Input
i = Input(shape=(28,28))

#flattens input layer
from keras.layers import Flatten
f = Flatten(input_shape=(28,28))
x = f(i)

#creates 3 dense (fully-coupled) layers for the model
from keras.layers import Dense
d = Dense(512, activation="relu", input_shape=(784,))
x2 = d(x)
d2 = Dense(512, activation="relu", input_shape=(512,))
x3 = d2(x2)
d3 = Dense(10, activation="softmax", input_shape=(512,))
o = d3(x3)

#imports model package from keras
from keras import Model

#imports RMSprop model optimization tool
from keras.optimizers import RMSprop

#sets up, runs, and tunes the model based on provided training and test data
model = Model(inputs=i, outputs=o)
model.compile( loss="categorical_crossentropy", optimizer=RMSprop(), metrics=["accuracy"])
model.fit(x_train, y_train, epochs=1)
model.evaluate(x_test, y_test)
