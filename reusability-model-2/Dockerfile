######### DOCKER BUILD PROCESS #########
# To run your Dockerfile you need to set your YOUR_DOCERHUB_NAME first
# Then build your Dockerfile by entering the command below.
# docker build -t $YOUR_DOCKERHUB_NAME/my-docker-repo .
########################################

######### DOCKER BUILD PROCESS #########
# After you have successfully built your docker you can run your docker image by entering the code below:
# docker run -t $YOUR_DOCKERHUB_NAME/my-docker-repo
########################################
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip git nano

RUN pip3 install numpy==1.16.4 pandas==0.25.0 keras==2.2.4 tensorflow==1.14.0 matplotlib==3.1.1 pillow==6.1.0 argparse==1.1 opencv-python==4.1.0.25

RUN apt-get install -y build-essential cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

RUN mkdir /usr/ml-project \
	&& cd /usr/ml-project

WORKDIR  /usr/ml-project

CMD git clone https://github.com/cyber-carpentry/group1-machine-learning-project.git \ 
	&& cd group1-machine-learning-project/reusability-model-2 \
	&& python3 build_model_reusability.py \ 
	&& /bin/bash
