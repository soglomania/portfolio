# Prometheus

[Django Prometheus Metrics](http://sogloarcadius.xyz/monitoring/metrics)

[Node-Exporter Prometheus Metrics](http://sogloarcadius.xyz:9100/metrics)

[Prometheus Server Metrics](http://sogloarcadius.xyz:9090/metrics)

[Prometheus UI](http://sogloarcadius.xyz:9090)

[Prometheus Web Console](http://sogloarcadius.xyz:9090/consoles/summary.html)

# Grafana Dashbord

[Grafana Dashboard](http://sogloarcadius.xyz:3000)

Default Credentials : admin/admin

# ELK

[Kibana Dashboard](http://sogloarcadius.xyz:5601)

# HTTPS

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
-d sogloarcadius.xyz -d www.sogloarcadius.xyz
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
-d sogloarcadius.xyz -d www.sogloarcadius.xyz

```


## Generate a 2048 bit DH Param file

```
mkdir -p /docker/portfolio/volumes/dh-param/
touch /docker/portfolio/volumes/dh-param/dhparam-2048.pem
sudo openssl dhparam -out /docker/portfolio/volumes/dh-param/dhparam-2048.pem 2048

```