def RepresentsInt(s):
        try:
                int(s)
                return True
        except ValueError:
                return False

def OptimizerSelection():
	print("Please Select the Optimizer [1,5] for the Model:\n")
	print("1) SDG\n")
	print("2) ADAM\n")
	print("3) RMSPROP")
	print("4) ADAGRAD")
	print("5) ADADELTA")
	selection = input()
	if selection=='1' :
		return 'sdg'
	elif selection=='2' :
		return 'adam'
	elif selection=='3' :
		return 'rmsprop'
	elif selection=='4' :
		return 'adagrad'
	elif selection=='5' :
		return 'adadelta'

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

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

type(train_images)

train_images = train_images / 255.0
test_images = test_images / 255.0

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#creates output image file that allow visualization of different class types

fig = plt.figure(figsize=(10,10))

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.savefig('item_viz.png')

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(3, activation=tf.nn.relu), 
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=selected_optimizer, 
    loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=num_of_epochs)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
