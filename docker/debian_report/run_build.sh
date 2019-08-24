
CONTAINER_PREFIX=yosukesan
CONTAINER_IMAGE_NAME="${CONTAINER_PREFIX}/debian-report"
CONTAINER_NAME=debian-report

#debug
docker events&

# build
docker image build -t ${CONTAINER_IMAGE_NAME} .

# publish
docker run --name ${CONTAINER_NAME} -d -p 22223:22 ${CONTAINER_IMAGE_NAME} 
