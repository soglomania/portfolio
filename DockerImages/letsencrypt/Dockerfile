

FROM nginx:latest


ENV CODE_DIR /usr/share/nginx/html

#chown -R nginx:nginx ${CODE_DIR} \

RUN mkdir -p ${CODE_DIR} && chmod 777 ${CODE_DIR}/ -R

COPY ./DockerImages/letsencrypt/nginx.conf /etc/nginx/conf.d/

COPY ./DockerImages/letsencrypt/index.html ${CODE_DIR}/

EXPOSE 80