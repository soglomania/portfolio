#!/bin/bash


read -p 'Username: ' username
read -p 'Email: ' email
read -sp 'Password: ' password
echo " "
echo "Username : $username"
echo "Email : $email"
echo "Password : $password"

python3 manage.py makemigrations

python3 manage.py migrate

# Create super user

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell

echo "Delete all users"
echo "import os; from django.contrib.auth.models import User; User.objects.all().delete()" | python3 manage.py shell

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell

echo "Create new super user"
echo "import os; from django.contrib.auth.models import User; User.objects.create_superuser('$username', '$email', '$password')" | python3 manage.py shell

echo "print all users"
echo "import os; from django.contrib.auth.models import User; print(User.objects.all())" | python3 manage.py shell

# UPDATE TABLES

# projects

python3 manage.py project --sql printall
python3 manage.py project --sql flush
python3 manage.py project --sql printall

python3 manage.py project --addproject ~/workspace/notebooks/portfolio/projects/software_development
python3 manage.py project --addproject ~/workspace/notebooks/portfolio/projects/data_science
python3 manage.py project --addproject ~/workspace/notebooks/portfolio/projects/computer_network
python3 manage.py project --addproject ~/workspace/notebooks/portfolio/projects/security


python3 manage.py project --sql printall


# About me
python3 manage.py resume --model PersonalInfo --sql printall
python3 manage.py resume --model PersonalInfo --sql flush
python3 manage.py resume --model PersonalInfo --sql printall

python3 manage.py resume --model PersonalInfo --addresume ~/workspace/notebooks/portfolio/about.me/

python3 manage.py resume --model PersonalInfo --sql printall


#Education
#python3 manage.py resume --model Education --sql printall
#python3 manage.py resume --model Education --sql flush
#python3 manage.py resume --model Education --sql printall

#python3 manage.py resume --model Education --addresume ~/workspace/notebooks/portfolio/education

#python3 manage.py resume --model Education --sql printall