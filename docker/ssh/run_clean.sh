
CONTAINER_PREFIX=yosukesan
CONTAINER_IMAGE_NAME=${CONTAINER_PREFIX}/debian-openssh-server
CONTAINER_NAME=debian-sshd

docker stop ${CONTAINER_NAME}
docker rm ${CONTAINER_NAME}
docker image rm ${CONTAINER_IMAGE_NAME}
