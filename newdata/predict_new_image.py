#pip install Pillow
from PIL import Image
from keras.models import model_from_json
import numpy
import os
import cv2

#resize the images
myimage=Image.open("modified_blue_jeans.jpeg")
image=myimage.resize((28,28),Image.ANTIALIAS)
image=image.convert('LA')
image.save("modified.png")

#structurize the image to predict
image=cv2.imread("modified.png",0).astype("float32").reshape(1,28,28)
image/=255
#print(image.shape,image.dtype,image)

#load json and create model
json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
#load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

#test with new images
pred = loaded_model.predict(image)
print(pred)
