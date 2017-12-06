
FROM nginx

###############################################################################
#                                INSTALLATION
###############################################################################

### install Filebeat same version as ELK
ENV FILEBEAT_VERSION 6.0.0


RUN apt-get update -qq \
 && apt-get install -qqy curl \
 && apt-get clean

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-amd64.deb \
 && dpkg -i filebeat-${FILEBEAT_VERSION}-amd64.deb \
 && rm filebeat-${FILEBEAT_VERSION}-amd64.deb


###############################################################################
#                                CONFIGURATION
###############################################################################

### configure Filebeat

# config file
ADD ./DockerImages/filebeat/filebeat.yml /etc/filebeat/filebeat.yml
RUN chmod 644 /etc/filebeat/filebeat.yml

# CA cert
RUN mkdir -p /etc/pki/tls/certs
ADD ./DockerImages/filebeat/logstash-beats.crt /etc/pki/tls/certs/logstash-beats.crt



###############################################################################
#                                    START
###############################################################################

ADD ./DockerImages/filebeat/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
CMD [ "/usr/local/bin/start.sh" ]
