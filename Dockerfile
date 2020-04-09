FROM ubuntu:18.04

LABEL maintainer.fullname="SOGLO Arcadius"
LABEL maintainer.email="rtsoglo@gmail.com"

## Default ubuntu docker image doesn't have en-US.UTF-8
RUN apt update --fix-missing && apt install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	gettext \
	git \
	build-essential \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	wget \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
	pip3 install uwsgi && \
   rm -rf /var/lib/apt/lists/*


ENV CODE_DIR /home/docker/code


COPY app/requirements.txt ${CODE_DIR}/app/
RUN pip3 install -r ${CODE_DIR}/app/requirements.txt

# Nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY confs/nginx-https.conf /etc/nginx/sites-available/default


# Supervisor
COPY confs/supervisor-app.conf /etc/supervisor/conf.d/

# uWSGI
COPY confs/uwsgi_params  ${CODE_DIR}/uwsgi_params
COPY confs/uwsgi.ini ${CODE_DIR}/uwsgi.ini


# App
COPY app ${CODE_DIR}/app
RUN python3 ${CODE_DIR}/app/manage.py collectstatic --no-input


# JWT
ARG JWT_PUBLIC_KEY
ARG JWT_PRIVATE_KEY

ENV JWT_PUBLIC_KEY $JWT_PUBLIC_KEY
ENV JWT_PRIVATE_KEY $JWT_PRIVATE_KEY


EXPOSE 80
EXPOSE 443

WORKDIR ${CODE_DIR}

CMD ["supervisord", "-n"]