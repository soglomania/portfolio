
USERNAME?=sogloarcadius
PASSWORD?=!AreYouAHacker!2018
EMAIL?=rtsoglo@gmail.com
PORTFOLIO_DATA_DIR?=$(PWD)/data/portfolio
PATH_TO_MANAGE_PY?=$(PWD)/website
APP_CLUSTER?=app
MONITORING_CLUSTER?=monitoring

deploy-app:
	make makemigrations
	make create-user
	make reset-db
	make start-app-cluster
	make clean-portfolio-data-dir

makemigrations:
	rm $(PATH_TO_MANAGE_PY)/db.sqlite && \
	cd $(PATH_TO_MANAGE_PY) && \
	python manage.py makemigrations && \
	python manage.py migrate

start-app-cluster:
	sudo docker-compose up --build -d $(APP_CLUSTER)

start-monitoring-cluster:
	sudo sysctl -w vm.max_map_count=262144 && \
	sudo docker-compose up --build -d $(MONITORING_CLUSTER)

stop-cluster:
	sudo docker-compose down --volumes


clean-portfolio-data-dir:
	-rm -rf $(PWD)/data 

pull-portfolio-data: clean-portfolio-data-dir
	mkdir -p data && cd data && \
	git clone https://github.com/soglomania/notebooks && \
	mv $(PWD)/data/notebooks/portfolio $(PWD)/data && rm -rf $(PWD)/data/notebooks

create-user:
	cd $(PATH_TO_MANAGE_PY) &&	pwd && echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell && \
	echo "Delete all users" && \
	echo "import os; from django.contrib.auth.models import User; User.objects.all().delete()" | python manage.py shell && \
	echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell && \
	echo "Create new super user" && \
	echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser('$(USERNAME)','$(EMAIL)','$(PASSWORD)')" | python manage.py shell && \
	echo "print all users" && \
	echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell && \
	cd ../ && pwd

reset-db: pull-portfolio-data
	cd $(PATH_TO_MANAGE_PY) && \
	python manage.py project --sql printall && \
	python manage.py project --sql flush && \
	python manage.py project --sql printall && \
	python manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/software_development && \
	python manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/data_science && \
	python manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/computer_network && \
	python manage.py project --addproject $(PORTFOLIO_DATA_DIR)/projects/security && \
	python manage.py project --sql printall && \
	python manage.py resume --model PersonalInfo --sql printall && \
	python manage.py resume --model PersonalInfo --sql flush && \
	python manage.py resume --model PersonalInfo --sql printall && \
	python manage.py resume --model PersonalInfo --addresume $(PORTFOLIO_DATA_DIR)/about.me/ && \
	python manage.py resume --model PersonalInfo --sql printall




