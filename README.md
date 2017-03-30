## Tensorflow + Keras container image [CPU | GPU]

* see requirements.txt in each folder for packages included
* see [Docker Hub](https://hub.docker.com/r/aleozlx/tkstack/tags/) for available tags
* see [GitHub](https://github.com/aleozlx/tkstack) for source files

## Tag naming convention

~~~ regex
aleozlx/tkstack:t(?P<tensorflow_version>\d{3})k(?P<keras_version>\d{3})(|-gpu)
~~~

**example**: `t101k202-gpu`

## Workspace structure

~~~ bash
    /workspace                      # run ide from here
    /workspace/project              # clone project source code
    /workspace/scripts              # mount other scripts / notebooks [optional]
    /workspace/datasets             # mount dataset
    "`python -m site --user-site`"  # user modules
~~~

## Example starter script

~~~ bash
#!/bin/bash

DOCKER="nvidia-docker"
DOCKER_RUN="-it"
IMAGE="aleozlx/tkstack:t101k202-gpu"

# Expose ports
let "P=8888"

PORTS="-p $((P++)):8888"

# Define file locations to be mounted from host here
PROJECT="$(readlink -f .)"
SCRIPTS="$(readlink -f ./notebooks)"
DATASETS="$(readlink -f ../datafiles)"

VOLUMNS="-v $PROJECT:/workspace/project -v $DATASETS:/workspace/datasets -v $SCRIPTS:/workspace/scripts"

# Launch
set -x
$DOCKER run $DOCKER_RUN $PORTS $VOLUMNS $IMAGE $DOCKER_CMD
~~~
