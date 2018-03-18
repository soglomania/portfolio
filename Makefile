
USERNAME?=sogloarcadius
PASSWORD?=!AreYouAHacker!2018
EMAIL?=rtsoglo@gmail.com
PORTFOLIO_DATA_DIR?=~/workspace/notebooks/portfolio
PATH_TO_MANAGE_PY?=$(PWD)/website
APP_CLUSTER?=app
MONITORING_CLUSTER?=monitoring
GRAFANA_SERVICE?=grafana

reset-database:
	make delete-database
	make makemigrations
	make create-user
	make insert-rows-db

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





