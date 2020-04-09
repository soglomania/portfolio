# Prometheus

[Django Prometheus Metrics](http://sogloarcadius.com/monitoring/metrics)

[Node-Exporter Prometheus Metrics](http://sogloarcadius.com:9100/metrics)

[Prometheus Server Metrics](http://sogloarcadius.com:9090/metrics)

[Prometheus UI](http://sogloarcadius.com:9090)

[Prometheus Web Console](http://sogloarcadius.com:9090/consoles/summary.html)

# Grafana Dashbord

[Grafana Dashboard](http://sogloarcadius.com:3000)

Default Credentials : admin/admin

# ELK

[Kibana Dashboard](http://sogloarcadius.com:5601)



# HTTPS CONFIGURATION STEPS


## Start letsencrypt nginx 

```
mkdir -p /docker/portfolio/volumes/letsencrypt-data/
cp ./docker/letsencrypt/index.html /docker/portfolio/volumes/letsencrypt-data/
sudo docker-compose -f docker-compose.base.yaml up --build -d letsencrypt
```


## Generate a 2048 bit DH Param file

```
mkdir -p /docker/portfolio/volumes/dh-param/
touch /docker/portfolio/volumes/dh-param/dhparam-2048.pem
sudo openssl dhparam -out /docker/portfolio/volumes/dh-param/dhparam-2048.pem 2048
```

## Issue a staging certificate

```
sudo docker run -it --rm \
-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
-v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--register-unsafely-without-email --agree-tos \
--webroot-path=/data/letsencrypt \
--staging \
-d sogloarcadius.com -d www.sogloarcadius.com
```

## Get information about certificate

```
sudo docker run --rm -it --name certbot \
-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
certbot/certbot \
--staging \
certificates
```

## Clean up Certificates

```
sudo rm -rf /docker/portfolio/volumes/

```

## Issue a production certificate

```
sudo docker run -it --rm \
-v /docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt \
-v /docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt \
-v /docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt \
-v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" \
certbot/certbot \
certonly --webroot \
--email rtsoglo@gmail.com --agree-tos --no-eff-email \
--webroot-path=/data/letsencrypt \
-d sogloarcadius.com -d www.sogloarcadius.com

```


## Add crontab to renew certificate

``` 
sudo crontab -e

0 23 * * * docker run --rm -it --name certbot -v "/docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt" -v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --quiet
```


## Rate https configuration

* [Security Headers](http://securityheaders.io)

* [HTTPS Implementation Qualys. SSL Labs](http://ssllabs.com)


# Video Tools

* Adobe Master Collection CS6 ( Photoshop, Adobe After Effects and Adobe Premiere)

* Vegas Pro (conseillé par Francois Leroux)

* Camtasia (Video Tutorials )

* Windows video maker


# ELK Troubleshooting

run on the server hosting docker machines to increase mem

``` 
$ sudo sysctl -w vm.max_map_count=262144

```


# Start app http

```sh

source production.properties

docker-compose -f docker-compose.base.yaml -f docker-compose.httponly.yaml build --build-arg JWT_PUBLIC_KEY --build-arg JWT_PRIVATE_KEY django

docker-compose -f docker-compose.base.yaml -f docker-compose.httponly.yaml up -d django

```


# Start app https

```sh

source production.properties

docker-compose -f docker-compose.base.yaml -f docker-compose.yaml build --build-arg JWT_PUBLIC_KEY --build-arg JWT_PRIVATE_KEY django

docker-compose -f docker-compose.base.yaml -f docker-compose.yaml up -d django

```


# Start elk

```sh

sysctl -w vm.max_map_count=262144

docker-compose -f docker-compose.base.yaml -f docker-compose.elk.yaml up --build -d filebeat

```

# Stop all containers

```sh

docker-compose -f docker-compose.base.yaml -f docker-compose.yaml -f docker-compose.httponly.yaml down --volumes

```
