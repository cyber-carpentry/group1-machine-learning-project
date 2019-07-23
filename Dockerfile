FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install numpy pandas sklearn keras tensorflow matplotlib pillow argparse

COPY src /g1-ml-project

WORKDIR /g1-ml-project
