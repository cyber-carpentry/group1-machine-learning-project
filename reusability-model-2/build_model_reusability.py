def RepresentsInt(s):
        try:
                int(s)
                return True
        except ValueError:
                return False

# Select the optimizer method
def OptimizerSelection():
	print("Please Select the Optimizer [1,5] for the Model:")
	print("1) SGD")
	print("2) ADAM")
	print("3) RMSPROP")
	print("4) ADAGRAD")
	print("5) ADADELTA")
	selection = input()
	if selection=='1' :
		return 'sgd'
	elif selection=='2' :
		return 'adam'
	elif selection=='3' :
		return 'rmsprop'
	elif selection=='4' :
		return 'adagrad'
	elif selection=='5' :
		return 'adadelta'

from keras.datasets import cifar10, cifar100, mnist, fashion_mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
selection=1
image_size=28
category_size=10

# Select the predefined datasets
def SelectDataset():
	print("Please Select the Dataset given [1-4] below:")
	print("1) CIFAR10")
	print("2) CIFAR100")
	print("3) MNIST")
	print("4) FASHION-MNIST")
	selection = input()
	if selection=='1' :
		return cifar10.load_data(), 32, 10, selection
	elif selection=='2' :
		return cifar100.load_data(label_mode='fine'), 32, 100, selection
	elif selection=='3' :
		return mnist.load_data(), 28, 10, selection
	elif selection=='4' :
		return fashion_mnist.load_data(), 28, 10, selection

#change number of epochs
import numpy
tmp_num_of_epochs='error'
num_of_epochs=1
while not RepresentsInt(tmp_num_of_epochs):
	tmp_num_of_epochs=input("Enter a number between [1,n] for defining the number of epochs\n")
	if not RepresentsInt(tmp_num_of_epochs):
		print("NOT A NUMBER")
num_of_epochs=int(str(tmp_num_of_epochs))

selected_optimizer=OptimizerSelection()

import keras, tensorflow as tf, numpy as np
#pip install matplotlib - needs to go in dockerfile!!!
import matplotlib.pyplot as plt
from keras.datasets import fashion_mnist

np.random.seed(1)
tf.set_random_seed(1)

# Run dataset selcetion function
#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
((x_train, y_train), (x_test, y_test)), image_size, category_size, selection=SelectDataset()

type(x_train)

x_train = x_train / 255.0
x_test = x_test / 255.0

#class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
#                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#creates output image file that allow visualization of different class types

#fig = plt.figure(figsize=(category_size,category_size))

#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(x_train[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[y_train[i]])
#plt.savefig('item_viz.png')
model = keras.Sequential([
	keras.layers.Flatten(input_shape=(image_size, image_size)),
	keras.layers.Dense(3, activation=tf.nn.relu), 
	keras.layers.Dense(category_size, activation=tf.nn.softmax)
])
if selection=='1' or selection=='2':
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(image_size, image_size, 3)),
		keras.layers.Dense(3, activation=tf.nn.relu), 
		keras.layers.Dense(category_size, activation=tf.nn.softmax)
	])
else:
	model = keras.Sequential([
		keras.layers.Flatten(input_shape=(image_size, image_size)),
		keras.layers.Dense(3, activation=tf.nn.relu), 
		keras.layers.Dense(category_size, activation=tf.nn.softmax)
	])

model.compile(optimizer=selected_optimizer, 
    loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=num_of_epochs)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

#sets up, runs, and tunes the model based on provided training and test data
from keras.models import model_from_json
import os

#create and save model as .json file
model_json = model.to_json()
with open("model.json", "w") as json_file:
        json_file.write(model_json)
model.save_weights("model.h5")
json_file.close()
