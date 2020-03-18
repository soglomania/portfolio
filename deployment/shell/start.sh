#!/bin/bash

read -p 'Service Name : ' name

#elk service exit because of the memory allowed issue
#command below fix the issue

sudo sysctl -w vm.max_map_count=262144

sudo docker-compose up --build -d $name
