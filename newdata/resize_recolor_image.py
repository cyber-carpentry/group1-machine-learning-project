#pip install Pillow
from PIL import Image
myimage=Image.open("new_images/blue_jeans.jpeg")
image=myimage.resize((28,28),Image.ANTIALIAS)
image=image.convert('LA')
image.save("modified_blue_jeans","png")
