FROM tensorflow/tensorflow:1.0.0
RUN apt-get -y update \
  && apt-get install -y build-essential vim git wget htop python-dev python-pip python-opencv
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip --no-cache-dir install -r /requirements.txt
COPY keras.json /root/.keras/keras.json
WORKDIR /notebooks
CMD /bin/bash
