RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install numpy pandas sklearn keras tensorflow matplotlib pillow argparse

WORKDIR /g1-ml-project
