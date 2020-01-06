FROM debian
LABEL maintainer="yosukesan"
RUN apt-get update && apt-get install -y nginx systemd
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
