#!/bin/bash

#elk service exit because of the memory allowed issue
#command below fix the issue
sudo sysctl -w vm.max_map_count=262144

# start main service in background (-d = detached)
sudo docker-compose up --build -d main
