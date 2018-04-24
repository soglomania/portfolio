FROM alpine:3.6

LABEL maintainer.fullname="SOGLO Arcadius"
LABEL maintainer.email="rtsoglo@gmail.com" 


# Install required packages and remove the apt packages cache when done.
# --no-cache avoid the use of apk add --update and rm -rf /var/cache/apk/* at end

RUN apk --no-cache add \	
	git \
	build-base \
	python3 \
	python3-dev \
	py-setuptools \
	py-pip \
	nginx \
	sqlite \ 
	uwsgi-rsyslog \
	supervisor \
	uwsgi-python3 && \
	pip install --upgrade pip


ENV CODE_DIR /home/docker/code

RUN mkdir -p ${CODE_DIR}/ && \
	chown -R nginx:nginx ${CODE_DIR} \
	&& chmod 777 ${CODE_DIR}/ \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R


# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY website/requirements.txt ${CODE_DIR}/app/
RUN pip3 install -r ${CODE_DIR}/app/requirements.txt

# setup all the configfiles
COPY configuration/nginx.conf /etc/nginx/nginx.conf
COPY configuration/nginx-app.conf /etc/nginx/conf.d/
COPY configuration/supervisor-app.conf /etc/supervisord.conf

# add (the rest of) our code
COPY website ${CODE_DIR}/website


# add configuration files
COPY configuration/uwsgi_params ${CODE_DIR}/uwsgi_params
COPY configuration/uwsgi.ini ${CODE_DIR}/uwsgi.ini

# Collect static files and media
RUN python3 ${CODE_DIR}/website/manage.py collectstatic --no-input

# Change owner of ${CODE_DIR}
RUN chown -R nginx:nginx ${CODE_DIR}/

EXPOSE 80

WORKDIR ${CODE_DIR}

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]