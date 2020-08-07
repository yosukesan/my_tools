FROM alpine:latest
LABEL maintainer="yosukesan"
EXPOSE 80

RUN apk add --update --no-cache nginx

ENTRYPOINT /usr/sbin/nginx -g "pid /tmp/nginx.pid; daemon off;" 
