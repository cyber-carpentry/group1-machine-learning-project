######### DOCKER BUILD PROCESS #########
# To run your Dockerfile you need to set your YOUR_DOCERHUB_NAME first
# Then build your Dockerfile by entering the command below.
# docker build -t $YOUR_DOCKERHUB_NAME/my-docker-repo .
########################################

######### DOCKER RUN PROCESS #########
# After you have successfully built your docker you can run your docker image by entering the code below:
# docker run -t $YOUR_DOCKERHUB_NAME/my-docker-repo
########################################

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip

# RUN pip3 install numpy pandas sklearn keras tensorflow matplotlib pillow argparse

RUN pip3 install keras tensorflow

RUN mkdir /app

COPY build_model.py /app

WORKDIR /app

CMD python3 build_model.py
