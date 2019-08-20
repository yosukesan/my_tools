
CONTAINER_PREFIX=yosukesan
CONTAINER_IMAGE_NAME="${CONTAINER_PREFIX}/debian-openssh-server"
CONTAINER_NAME=debian-sshd

# build
docker image build -t ${CONTAINER_IMAGE_NAME} .

# publish
docker run --name ${CONTAINER_NAME} -d -p 22222:22 ${CONTAINER_IMAGE_NAME} 
