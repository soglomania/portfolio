#!/bin/bash


read -p 'Username: ' username
read -p 'Email: ' email
read -sp 'Password: ' password
echo " "
echo "Username : $username"
echo "Email : $email"
echo "Password : $password"

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
echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser('$username', '$email', '$password')" | python manage.py shell

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python manage.py shell

# UPDATE TABLES

# projects

python manage.py project --sql printall

python manage.py project --sql flush

python manage.py project --sql printall

#software_development
python manage.py project --addproject ~/workspace/notebooks/portfolio/projects/software_development

#data_science
python manage.py project --addproject ~/workspace/notebooks/portfolio/projects/data_science

#computer_network
python manage.py project --addproject ~/workspace/notebooks/portfolio/projects/computer_network

#security
python manage.py project --addproject ~/workspace/notebooks/portfolio/projects/security


python manage.py project --sql printall


# personalinfos, education, ....

python manage.py resume --model PersonalInfo --sql printall

python manage.py resume --model PersonalInfo --sql flush

python manage.py resume --model PersonalInfo --sql printall

python manage.py resume --model PersonalInfo --addresume ~/workspace/notebooks/portfolio/resume/

python manage.py resume --model PersonalInfo --sql printall
 