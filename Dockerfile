FROM tensorflow/tensorflow:1.0.1
MAINTAINER Alex Yang <aleozlx@gmail.com>
RUN apt-get -y update \
  && apt-get install -y build-essential vim git wget htop python-dev python-pip python-opencv
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip --no-cache-dir install -r /requirements.txt
WORKDIR /notebooks
CMD /bin/bash

