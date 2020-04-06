
DJANGO_USERNAME?=admin
DJANGO_PASSWORD?=admin
DJANGO_EMAIL?=admin@admin.com

JUPYTER_DIR?=$(PWD)/data/jupyter
YAML_DIR?=$(PWD)/data/yaml
DJANGO_APP_DIR?=$(PWD)/app

SERVICE_APP?=django
SERVICE_LETSENCRYPT?=letsencrypt
SERVICE_ELK?=filebeat


reset-database:
	make delete-database && \
	make makemigrations && \
	make create-user && \
	make insert-yaml-dir

delete-database: 
	-rm $(DJANGO_APP_DIR)/db.sqlite

makemigrations:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate

start-app-http:
	sudo docker-compose -f docker-compose.base.yaml -f docker-compose.httponly.yaml up --build -d $(SERVICE_APP)

start-app-https:
	sudo docker-compose -f docker-compose.base.yaml -f docker-compose.yaml up --build -d $(SERVICE_APP)

start-elk:
	sudo sysctl -w vm.max_map_count=262144 && \
	sudo docker-compose up --build -d $(SERVICE_ELK) 

start-letsencrypt:
	sudo mkdir -p /docker/portfolio/volumes/letsencrypt-data/ && \
	sudo docker-compose -f docker-compose.base.yaml up --build -d $(SERVICE_LETSENCRYPT)

stop-cluster:
	sudo docker-compose -f docker-compose.base.yaml -f docker-compose.yaml -f docker-compose.httponly.yaml down --volumes


create-user:
	cd $(DJANGO_APP_DIR) &&	python3 --version && pwd && echo "print all users" && \
	echo "import os; from apps.users.models import User; print(User.objects.all())" | python3 manage.py shell && \
	echo "Delete all users" && \
	echo "import os; from apps.users.models import User; User.objects.all().delete()" | python3 manage.py shell && \
	echo "print all users" && \
	echo "import os; from apps.users.models import User; print(User.objects.all())" | python3 manage.py shell && \
	echo "Create new super user" && \
	echo "import os; from apps.users.models import User; User.objects.create_superuser('$(DJANGO_USERNAME)','$(DJANGO_EMAIL)','$(DJANGO_PASSWORD)')" | python3 manage.py shell && \
	echo "print all users" && \
	echo "import os; from apps.users.models import User; print(User.objects.all())" | python3 manage.py shell && \
	cd ../ && pwd

insert-jupyter-dir:
	cd $(DJANGO_APP_DIR) && python3 --version && jupyter --version && \
	echo "import tornado; print(tornado.version)" | python3 && \
	python3 manage.py project --db select && \
	python3 manage.py project --db flush && \
	python3 manage.py project --db select && \
	python3 manage.py project --addjupyter $(JUPYTER_DIR)/projects/software_development &&\
	python3 manage.py project --addjupyter $(JUPYTER_DIR)/projects/data_science && \
	python3 manage.py project --addjupyter $(JUPYTER_DIR)/projects/computer_network && \
	python3 manage.py project --addjupyter $(JUPYTER_DIR)/projects/security && \
	python3 manage.py project --db select && \
	python3 manage.py resume --model Biography --db select && \
	python3 manage.py resume --model Biography --db flush && \
	python3 manage.py resume --model Biography --db select && \
	python3 manage.py resume --model Biography --addjupyter $(JUPYTER_DIR)/biography/ && \
	python3 manage.py resume --model Biography --db select

insert-yaml-dir:
	cd $(DJANGO_APP_DIR) && python3 --version && \
	python3 manage.py project --db select && \
	python3 manage.py project --db flush && \
	python3 manage.py project --db select && \
	python3 manage.py project --addyaml $(YAML_DIR)/projects/dit.pentest.yaml &&\
	python3 manage.py project --addyaml $(YAML_DIR)/projects/graph_theory.yaml &&\
	python3 manage.py project --db select && \
	python3 manage.py resume --model Biography --db select && \
	python3 manage.py resume --model Biography --db flush && \
	python3 manage.py resume --model Biography --db select && \
	python3 manage.py resume --model Biography --addyaml $(YAML_DIR)/resume/biography.yaml && \
	python3 manage.py resume --model Biography --db select


certificate-create-staging: stop-cluster start-letsencrypt
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


certificate-show-staging:
	sudo docker run --rm -it --name certbot \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	certbot/certbot \
	--staging \
	certificates

certificate-generate-dh-param-file:
	sudo mkdir -p /docker/portfolio/volumes/dh-param/ && \
	sudo touch /docker/portfolio/volumes/dh-param/dhparam-2048.pem && \
	sudo openssl dhparam -out /docker/portfolio/volumes/dh-param/dhparam-2048.pem 2048


certificate-create-production: generate-dh-param-file stop-cluster start-letsencrypt
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

certificate-show-production:
	sudo docker run --rm -it --name certbot \
	-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
	-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
	-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
	certbot/certbot \
	certificates