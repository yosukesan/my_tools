
CONTAINER_PREFIX=yosukesan
CONTAINER_NAME=alpine_npm
CONTAINER_IMAGE_NAME="${CONTAINER_PREFIX}/${CONTAINER_NAME}"

docker image  build -t ${CONTAINER_IMAGE_NAME} .

# start as deamon 
#docker run -it --name ${CONTAINER_NAME} -d ${CONTAINER_IMAGE_NAME}
