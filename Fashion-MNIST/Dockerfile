######### DOCKER BUILD PROCESS #########
# To run your Dockerfile you need to set your YOUR_DOCKERHUB_NAME first
# At command prompt: YOUR_DOCKERHUB_NAME=<your dockerhub ID>
# Then build your Dockerfile by entering the command below.
# docker build -t $YOUR_DOCKERHUB_NAME/my-docker-repo .
########################################

######### DOCKER BUILD PROCESS #########
# After you have successfully built your docker you can run your docker image by entering the code below:
# docker run -t $YOUR_DOCKERHUB_NAME/my-docker-repo
########################################
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip git

RUN pip3 install numpy==1.16.4 pandas==0.25.0 keras==2.2.4 tensorflow==1.14.0 matplotlib==3.1.1 pillow==6.1.0 argparse==1.1

RUN mkdir /usr/ml-project \
	&& cd /usr/ml-project \
	&& git clone https://github.com/cyber-carpentry/group1-machine-learning-project.git

WORKDIR  /usr/ml-project/group1-machine-learning-project/Fashion-MNIST

CMD python3 build_model_fashionmnist.py
