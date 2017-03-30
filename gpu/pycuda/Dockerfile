FROM tensorflow/tensorflow:1.0.1-gpu-py3
MAINTAINER Alex Yang <aleozlx@gmail.com>

# System dependencies
RUN apt-get -y update && apt-get install -y build-essential vim git wget htop python3-dev python3-pip

# PyCUDA
RUN apt-get install -y libboost-all-dev python3-numpy python3-setuptools libboost-python-dev libboost-thread-dev
RUN cd /tmp && curl https://pypi.python.org/packages/e8/3d/4b6b622d8a22cace237abad661a85b289c6f0803ccfa3d2386103307713c/pycuda-2016.1.2.tar.gz | tar xvz
RUN cd /tmp/pycuda-2016.1.2 && python3 configure.py --python-exe=/usr/bin/python3 --cuda-root=/usr/local/cuda --cudadrv-lib-dir=/usr/lib/x86_64-linux-gnu --boost-inc-dir=/usr/include --boost-lib-dir=/usr/lib --boost-python-libname=boost_python-py34 --boost-thread-libname=boost_thread --no-use-shipped-boost && make -j 4
RUN cd /tmp/pycuda-2016.1.2 && python3 setup.py install && pip3 install .

# Python packages
#COPY requirements.txt /requirements.txt
#RUN pip3 install --upgrade pip && pip3 --no-cache-dir install -r /requirements.txt

# Customize Jupyter
#COPY custom.css /root/.jupyter/custom/custom.css

# Create workespace
RUN mkdir -p /workspace "`python3 -m site --user-site`"
WORKDIR /workspace
CMD /bin/bash

