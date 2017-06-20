## Tensorflow + Keras container image [CPU | GPU]

* see requirements.txt in each folder for packages included
* see [Docker Hub](https://hub.docker.com/r/aleozlx/tkstack/tags/) for available tags

## Tag naming convention

For latest GPU version
+ aleozlx/tkstack:latest

For specific version
+ aleozlx/tkstack:t<tensorflow_version>k<keras_version>
+ aleozlx/tkstack:t<tensorflow_version>k<keras_version>-gpu

**example**: `aleozlx/tkstack:t120k205-gpu`

## Workspace structure

~~~ bash
    /workspace                      # run ide from here
    /workspace/project              # clone project source code
    /workspace/scripts              # mount other scripts / notebooks [optional]
    /workspace/datasets             # mount dataset
    "`python -m site --user-site`"  # user modules
~~~

## Example starter script

see `docker-example.py` or `docker-example.sh`
