#!/bin/bash

sudo docker build -t  soglomania/portfolio .
sudo docker stop portfolio
sudo docker rm portfolio 
sudo docker rmi soglomania/portfolio:current  
sudo docker tag soglomania/portfolio:latest soglomania/portfolio:current   
sudo docker run -p 8080:80 -d --name portfolio soglomania/portfolio:latest 