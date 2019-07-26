## Reproducibility and Reusability of Deep Neural Networks with MNIST & Fashion-MNIST Datasets

This project aims to improve the reproducibility and reusability of deep neural network models trained using the MNIST and Fashion-MNIST datasets. In terms of reproducibility, it aims to improve the automatization of model training using existing datasets, established neural network architecture, and fixed machine learning parameters. In terms of reusability, it provides several options, including reusing the generated model with different datasets and reusing datasets with different neural network models. 

This project provides Docker images that have been prepared with all necessary packages installed to build some basic neural network models that are tuned for MNIST and Fashion-MNIST datasets. It will allow anyone to gain some exposure to deep learning models but do not have experience or do not want to spend time with coding and debugging.  Please refer to the instructions below for how to set up these basic models and how to modify them to run with different data sets.

### Group Members
* Natalie Chin
* Kaiwen Chen
* Ekincan Ufuktepe

### Hands-on Instructions for Running Docker Images

1. Log-on to a machine that is prepared with Docker Hub.  It can be your own computer, a Jetstream instance or other virtual machine.  If you use a Jetstream instance, a medium sized instance of Ubuntu 18.04 Devel and Docker v1.22 is suggested.

2. From the command line interface, docker pull the image from Docker Hub (see below for image descriptions).

 `$ docker pull <image>`
 
 For example:  `$ docker pull ekincanufuktepe/mnist-reproducability`

3. Use docker to run the desired image (see below for image descriptions).

 `$ docker run -it <image>`
 
 For example:  `$ docker run -it ekincanufuktepe/mnist-reproducability`

4. If applicable, follow the prompts to get the model built and trained.

5. To exit the container, type the following at the command prompt:

 `$ exit`

### Description of Deliverables
 
All of these deliverables have been published as Docker Hub images and can be easily used simply by running a Docker Hub container. 
  
#### 1) Reproducing basic neural network models for MNIST and Fashion-MNIST

MNIST: `docker pull ekincanufuktepe/mnist-reproducability`

Fashion-MNIST: `docker pull ekincanufuktepe/fashion-mnist-reproducability`

These two docker images will build containers that provide basic trained neural network models for the MNIST and Fashion-MNIST dataset, respectively.  The MNIST model is set to run using 1 epoch and the RMS optimization scheme.  The Fashion-MNIST model is set to run using 4 epochs and the Adam optimization scheme.  Sample output is provided in each of the docker containers, which a new user can compare with their own output to determine if the model builds have run successfully.

#### 2) Modifying basic neural network models for MNIST and Fashion-MNIST

MNIST: `docker pull ekincanufuktepe/mnist-reusability`

Fashion-MNIST: `docker pull ekincanufuktepe/fashion-mnist-reusability`

These two docker images will create containers that build basic trained neural network models for the MNIST and Fashion-MNIST dataset, respectively, that can be adjusted based on user input.  Users can change the number of epochs and/or the optimization scheme for each model to try and improve reliability and reduce loss.

#### 3) Replicability of basic neural network models for MNIST and Fashion-MNIST 

##### Model #1
`docker pull ekincanufuktepe/reusability-model-1`

##### Model #2
`docker pull ekincanufuktepe/reusability-model-2`

These two docker images will build containers that have a different number of hidden layers (2 and 1, respectively) and a different number of nodes than the original model (512 and 3, respectively).  These differences illustrate how the number of layers and nodes can affect model accuracy and loss.  Users are prompted to change the number of epochs and/or optimization scheme and can select from a few different training and test data sets.

#### 4) Reusability of datasets

The scripts in this directory allow the user to import new images and process them using the predict_new_image.py python script, which will resize and recolor them for model processing, as well as run them through a saved model, which provides a prediction for what it thinks the image  contains according to the original ten classes.  The directory contains a few sample images, which are names "modified_<name_of_item>.jpeg".

*In order to run this script, docker build must be run for Model #2 above.

 `docker pull ekincanufuktepe/reusability-model-2`

 `docker run -it ekincanufuktepe/reusability-model-2`
 
 - make sure to select Fashion-MNIST as the training and test data set (3rd prompt)

  *`apt-get install python-opencv` (You don't need this steps after 10:00am July 26, 2019)
 
  *which country choose "2", which time zone choose "105" (for some reasons, opencv can't be built into an image)
 
 `cd ../newimages/`

 `python3 predict_new_image.py` #modify this script to change the image that you are analyzing
