FROM tensorflow/tensorflow:1.0.1-gpu-py3
MAINTAINER Alex Yang <aleozlx@gmail.com>
RUN apt-get -y update \
  && apt-get install -y build-essential vim git wget htop python3-dev python3-pip
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip \
  && pip3 --no-cache-dir install -r /requirements.txt
WORKDIR /notebooks
CMD /bin/bash

