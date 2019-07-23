FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install numpy pandas sklearn keras tensorflow matplotlib pillow argparse

COPY build_model.py /home/jovyan/work/

WORKDIR /g1-ml-project
