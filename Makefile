
USERNAME?=$(DJANGO_USERNAME)
PASSWORD?=$(DJANGO_PASSWORD)
EMAIL?=$(DJANGO_EMAIL)

PORTFOLIO_DATA_DIR?=~/workspace/notebooks/portfolio
PATH_TO_MANAGE_PY?=$(PWD)/website
APP_CLUSTER?=app
MONITORING_CLUSTER?=monitoring
LETSENCRYPT_SERVICE?=letsencrypt
GRAFANA_SERVICE?=grafana

reset-database:
	make load-django-credentials && \
	make delete-database && \
	make makemigrations && \
	make create-user && \
	make insert-rows-db

encrypt-django-credentials:
	ansible-vault encrypt secrets.properties

decrypt-django-credentials:
	ansible-vault decrypt secrets.properties 

load-django-credentials:
	make decrypt-django-credentials
	$(source secrets.properties)
	make encrypt-django-credentials


delete-database: 
	-rm $(PATH_TO_MANAGE_PY)/db.sqlite

makemigrations:
	cd $(PATH_TO_MANAGE_PY) && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate

start-app-cluster:
	sudo docker-compose up --build -d $(APP_CLUSTER)

start-monitoring-cluster:
	sudo sysctl -w vm.max_map_count=262144 && \
	sudo docker-compose up --build -d $(MONITORING_CLUSTER)

start-grafana:
	sudo docker-compose up --build -d $(GRAFANA_SERVICE)

start-letsencrypt:
	sudo mkdir -p /docker/portfolio/volumes/letsencrypt-data/ && \
	sudo docker-compose up --build -d $(LETSENCRYPT_SERVICE)

stop-cluster:
	sudo docker-compose down --volumes


clean-portfolio-data-dir:
	-rm -rf $(PWD)/data/ 

pull-portfolio-data: clean-portfolio-data-dir
	mkdir -p --mode=777 $(PWD)/data && cd $(PWD)/data && \
	git clone https://github.com/soglomania/notebooks.git && \
	chmod -R 777 $(PWD)/data/ && \
	chown -R $(whoami):$(whoami) $(PWD)/data/ && ls -lsa

create-user:
	cd $(PATH_TO_MANAGE_PY) &&	python3 --version && pwd && echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell && \
	echo "Delete all users" && \
	echo "import os; from django.contrib.auth.models import User; User.objects.all().delete()" | python3 manage.py shell && \
	echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell && \
	echo "Create new super user" && \
	echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser('$(USERNAME)','$(EMAIL)','$(PASSWORD)')" | python3 manage.py shell && \
	echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell && \
	cd ../ && pwd

insert-rows-db:
	cd $(PATH_TO_MANAGE_PY) && python3 --version && jupyter --version && \
	echo "import tornado; print(tornado.version)" | python3 && \
	python3 manage.py project --sql printall && \
	python3 manage.py project --sql flush && \
	python3 manage.py project --sql printall && \
	python3 manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/software_development &&\
	python3 manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/data_science && \
	python3 manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/computer_network && \
	python3 manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/security && \
	python3 manage.py project --sql printall && \
	python3 manage.py resume --model PersonalInfo --sql printall && \
	python3 manage.py resume --model PersonalInfo --sql flush && \
	python3 manage.py resume --model PersonalInfo --sql printall && \
	python3 manage.py resume --model PersonalInfo --addresume $(PORTFOLIO_DATA_DIR)/about.me/ && \
	python3 manage.py resume --model PersonalInfo --sql printall



create-certificate-staging: stop-cluster start-letsencrypt
	sudo docker run -it --rm \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	-v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" \
	certbot/certbot \
	certonly --webroot \
	--register-unsafely-without-email --agree-tos \
	--webroot-path=/data/letsencrypt \
	--staging \
	-d sogloarcadius.com -d www.sogloarcadius.com

show-certificate-staging:
	sudo docker run --rm -it --name certbot \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	certbot/certbot \
	--staging \
	certificates

generate-dh-param-file:
	sudo mkdir -p /docker/portfolio/volumes/dh-param/ && \
	sudo touch /docker/portfolio/volumes/dh-param/dhparam-2048.pem && \
	sudo openssl dhparam -out /docker/portfolio/volumes/dh-param/dhparam-2048.pem 2048

create-certificate-production: generate-dh-param-file stop-cluster start-letsencrypt
	sudo docker run -it --rm \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	-v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" \
	certbot/certbot \
	certonly --webroot \
	--email rtsoglo@gmail.com --agree-tos --no-eff-email \
	--webroot-path=/data/letsencrypt \
	-d sogloarcadius.com -d www.sogloarcadius.com

show-certificate-production:
	sudo docker run --rm -it --name certbot \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	certbot/certbot \
	certificates