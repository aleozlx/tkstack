FROM tensorflow/tensorflow:1.3.0-gpu-py3
MAINTAINER Alex Yang <aleozlx@gmail.com>

# System dependencies
RUN apt-get -y update && apt-get install -y build-essential vim wget htop python3-dev python3-pip

# Python packages
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 --no-cache-dir install -r /requirements.txt

# Create workespace
RUN mkdir -p /workspace "`python3 -m site --user-site`"
WORKDIR /workspace
CMD /bin/bash
