FROM alpine:3.6

LABEL maintainer.fullname="SOGLO Arcadius"
LABEL maintainer.email="rtsoglo@gmail.com" 


# Install required packages and remove the apt packages cache when done.
# --no-cache avoid the use of apk add --update and rm -rf /var/cache/apk/* at end

ENV SUPERVISOR_VERSION=3.3.1

RUN apk --no-cache add \	
	git \
	build-base \
	python3 \
	python3-dev \
	py-setuptools \
	py-pip \
	nginx \
	sqlite \ 
	uwsgi-python3 && \
	pip install --upgrade pip && \
	pip install supervisor==$SUPERVISOR_VERSION


# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY website/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY configuration/nginx-app.conf /etc/nginx/sites-available/default
COPY configuration/supervisor-app.conf /etc/supervisord.conf

# add (the rest of) our code
COPY website /home/docker/code/website

#Change working directory
RUN  cd /home/docker/code

# add configuration files
COPY configuration/uwsgi_params /home/docker/code/uwsgi_params
COPY configuration/uwsgi.ini /home/docker/code/uwsgi.ini

#WORKDIR /home/docker/code/
RUN python3 /home/docker/code/website/manage.py collectstatic --no-input

EXPOSE 80
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]