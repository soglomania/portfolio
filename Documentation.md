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

## Copy letsencrypt nginx files 

```
cp ./DockerImages/letsencrypt/index.html /docker/portfolio/volumes/letsencrypt-data/

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


## Generate a 2048 bit DH Param file

```
mkdir -p /docker/portfolio/volumes/dh-param/
touch /docker/portfolio/volumes/dh-param/dhparam-2048.pem
sudo openssl dhparam -out /docker/portfolio/volumes/dh-param/dhparam-2048.pem 2048

```

## Add crontab to renew certificate

``` 
sudo crontab -e

0 23 * * * docker run --rm -it --name certbot -v "/docker/portfolio/volumes/etc/letsencrypt:/etc/letsencrypt" -v "/docker/portfolio/volumes/var/lib/letsencrypt:/var/lib/letsencrypt" -v "/docker/portfolio/volumes/letsencrypt-data:/data/letsencrypt" -v "/docker/portfolio/volumes/var/log/letsencrypt:/var/log/letsencrypt" certbot/certbot renew --quiet
```


## Rate https configuration

* [Security Headers](http://securityheaders.io)

* [HTTPS Implementation Qualys. SSL Labs](http://ssllabs.com)