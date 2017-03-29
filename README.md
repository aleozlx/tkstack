## Tensorflow + Keras container image

* see requirements.txt in each folder for packages included
* see [Docker Hub](https://hub.docker.com/r/aleozlx/tkstack/tags/) for available tags

## Workspace structure

~~~ bash
    /workspace                      # run ide from here
    /workspace/project              # clone project source code
    /workspace/scripts              # mount other scripts / notebooks [optional]
    /workspace/datasets             # mount dataset
    "`python -m site --user-site`"  # user modules
~~~
