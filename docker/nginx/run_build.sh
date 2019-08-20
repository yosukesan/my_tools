
CONTAINER_PREFIX=yosukesan
CONTAINER_IMAGE_NAME="${CONTAINER_PREFIX}/debian-nginx"
CONTAINER_NAME=debian-httpd

docker image  build -t ${CONTAINER_IMAGE_NAME} .

docker run --name ${CONTAINER_NAME} -d -p 8888:80 ${CONTAINER_IMAGE_NAME}
