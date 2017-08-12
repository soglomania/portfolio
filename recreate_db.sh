#!/bin/bash

python manage.py makemigrations

python manage.py migrate

# Create super user

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell

echo "Delete all users"
echo "import os; from django.contrib.auth.models import User; User.objects.all().delete()" | python manage.py shell

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell

echo "Create new super user"
echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser(os.environ['username'], os.environ['email'], os.environ['password'])" | python manage.py shell

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell

# UPDATE TABLES

# projects

python manage.py portfolio --sql printall

python manage.py portfolio --sql flush

python manage.py portfolio --sql printall

python manage.py portfolio --addproject ~/workspace/notebooks/portfolio/projects/

python manage.py portfolio --sql printall


# Resume

#Personal Infos
python manage.py resume --model PersonalInfo --sql printall

python manage.py resume --model PersonalInfo --sql flush

python manage.py resume --model PersonalInfo --sql printall

python manage.py resume --model PersonalInfo --addresume ~/workspace/notebooks/portfolio/resume/

python manage.py resume --model PersonalInfo --sql printall
 