#!/bin/bash

CWD=`pwd`
CMD=node
IMAGE=yosukesan/alpine_npm 
echo "sdfsdf" | docker run -i --rm --name test -v ${CWD}:/tmp -w /tmp ${IMAGE} ${CMD} sample.js
#docker run -it --rm --name test -v ${CWD}:/tmp -w /tmp ${IMAGE} ${CMD} main.js
