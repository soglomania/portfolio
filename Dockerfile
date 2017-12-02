FROM ubuntu:16.04

LABEL maintainer.fullname="SOGLO Arcadius"
LABEL maintainer.email="rtsoglo@gmail.com" 




# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi


# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY website/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY configuration/nginx-app.conf /etc/nginx/sites-available/default
COPY configuration/supervisor-app.conf /etc/supervisor/conf.d/

# add (the rest of) our code
COPY website /home/docker/code/website

# add configuration files
COPY configuration/uwsgi_params /home/docker/code/uwsgi_params
COPY configuration/uwsgi.ini /home/docker/code/uwsgi.ini

#WORKDIR /home/docker/code/
RUN python3 /home/docker/code/website/manage.py collectstatic --no-input

EXPOSE 80
CMD ["supervisord", "-n"]