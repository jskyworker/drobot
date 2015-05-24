FROM docker.io/mongo
MAINTAINER Y. Mykhailin <jskyworker@gmail.com>

ADD ./ /flask


RUN \
  rm -fr /flask/.git ;\
  apt-get update && apt-get -y install python python-pip procps supervisor ;\
  pip install pymongo flask
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8080
CMD ["/usr/bin/supervisord"]