
FROM debian:sid
LABEL maintainer = "yosukesan"

RUN apt-get update && apt-get install -y apt-utils \
    openssh-server \
    git \
    locales \
    lv \
    make \
    poppler-data \
    python3-pygments \
    texlive-lang-japanese \
    texlive-latex-extra \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-plain-generic \
    ghostscript-x \
    evince

RUN mkdir /var/run/sshd
#RUN echo `openssl rand -base64 32` | chpasswd | tee
RUN echo 'root:ytest' | chpasswd 

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication/PasswordAuthentication/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
