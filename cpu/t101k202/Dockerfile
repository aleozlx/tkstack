FROM tensorflow/tensorflow:1.0.1
MAINTAINER Alex Yang <aleozlx@gmail.com>
RUN apt-get -y update \
  && apt-get install -y build-essential vim git wget htop python-dev python-pip python-opencv
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip --no-cache-dir install -r /requirements.txt
RUN mkdir -p /workspace/{project,datasets} "`python -m site --user-site`"
WORKDIR /workspace
CMD /bin/bash
