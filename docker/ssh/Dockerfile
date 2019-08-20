
FROM debian
LABEL maintainer = "yosukesan"

RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y openssh-server systemd
RUN mkdir /var/run/sshd

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
