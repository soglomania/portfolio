DJANGO_USERNAME?=admin
DJANGO_PASSWORD?=admin
DJANGO_EMAIL?=admin@admin.com

JUPYTER_DIR?=$(PWD)/data/jupyter
YAML_DIR?=$(PWD)/data/yaml
DJANGO_APP_DIR?=$(PWD)/app

setup:
	-rm $(DJANGO_APP_DIR)/db.sqlite && \
	make makemigrations && \
	make create-superuser && \
	make insert-biography && \
	make insert-languages && \
	make insert-educations && \
	make insert-experiences && \
	make insert-skills && \
	make insert-interests && \
	make insert-projects 


makemigrations:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate


create-superuser:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py users --db select && \
	python3 manage.py users --db flush && \
	python3 manage.py users --db select && \
	python3 manage.py users --email $(DJANGO_EMAIL) --username $(DJANGO_USERNAME)  --password $(DJANGO_PASSWORD) && \
	python3 manage.py users --db select

insert-biography:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model biography --db select && \
	python3 manage.py portfolio --model biography --db flush && \
	python3 manage.py portfolio --model biography --db select && \
	python3 manage.py portfolio --model biography --addjupyter $(JUPYTER_DIR)/biography/ && \
	python3 manage.py portfolio --model biography --db select


insert-languages:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model language --db select && \
	python3 manage.py portfolio --model language --db flush && \
	python3 manage.py portfolio --model language --db select && \
	python3 manage.py portfolio --model language --addyaml $(YAML_DIR)/languages/english.yaml &&\
	python3 manage.py portfolio --model language --addyaml $(YAML_DIR)/languages/french.yaml &&\
	python3 manage.py portfolio --model language --addyaml $(YAML_DIR)/languages/spanish.yaml &&\
	python3 manage.py portfolio --model project --db select


insert-educations:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model education --db select && \
	python3 manage.py portfolio --model education --db flush && \
	python3 manage.py portfolio --model education --db select && \
	python3 manage.py portfolio --model education --addyaml $(YAML_DIR)/educations/ingenieur.enssat.yaml &&\
	python3 manage.py portfolio --model education --db select


insert-experiences:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model experience --db select && \
	python3 manage.py portfolio --model experience --db flush && \
	python3 manage.py portfolio --model experience --db select && \
	python3 manage.py portfolio --model experience --addyaml $(YAML_DIR)/experiences/apprenti.ingénieur.yaml &&\
	python3 manage.py portfolio --model experience --db select



insert-skills:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model skill --db select && \
	python3 manage.py portfolio --model skill --db flush && \
	python3 manage.py portfolio --model skill --db select && \
	python3 manage.py portfolio --model skill --addyaml $(YAML_DIR)/skills/programming.yaml &&\
	python3 manage.py portfolio --model skill --db select


insert-interests:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model interest --db select && \
	python3 manage.py portfolio --model interest --db flush && \
	python3 manage.py portfolio --model interest --db select && \
	python3 manage.py portfolio --model interest --addyaml $(YAML_DIR)/interests/traveling.yaml &&\
	python3 manage.py portfolio --model interest --db select



insert-projects:
	cd $(DJANGO_APP_DIR) && \
	python3 manage.py portfolio --model project --db select && \
	python3 manage.py portfolio --model project --db flush && \
	python3 manage.py portfolio --model project --db select && \
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/bike_sharing.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/connect4.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/data_wrangling.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/eigenfaces.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/employee_management.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/feelshare.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/graph_theory.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/judo.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/machine_learning_sql.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/network_redesign.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/pentest.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/serveur_messagerie.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/ski_reservation.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/uml_iot_application.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/uml_loyalty_system.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/weka_machine_learning.yaml &&\
	python3 manage.py portfolio --model project --addyaml $(YAML_DIR)/projects/wordpress_ufcr.yaml &&\
	python3 manage.py portfolio --model project --db select