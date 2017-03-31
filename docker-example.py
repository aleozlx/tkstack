#!/usr/bin/python
from __future__ import print_function
import os, sys

DOCKER="nvidia-docker"
DOCKER_RUN="-it"
IMAGE="aleozlx/tkstack:research-gpu"

PORTS = ['-p', '8888:8888']

PROJECT = os.path.abspath(".")
SCRIPTS = os.path.abspath("notebooks")
DATASETS = os.path.abspath("../datafiles")

VOLUMNS = ['-v', PROJECT+':/workspace/project', '-v', DATASETS+':/workspace/datasets', '-v', SCRIPTS+':/workspace/scripts']

if len(sys.argv)>1:
    # Start docker and do something without exposing ports
    os.execvp(DOCKER, [DOCKER, 'run', DOCKER_RUN] + PORTS + VOLUMNS + [IMAGE] + sys.argv[1:])
else:
    # Start docker and enter shell
    argv = [DOCKER, 'run', DOCKER_RUN] + PORTS + VOLUMNS + [IMAGE]
    print(' '.join(map(lambda i: ("'%s'"%i) if ' ' in i else i, argv)))
    os.execvp(DOCKER, argv)
