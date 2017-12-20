FROM prom/prometheus:v1.8.0


ADD ./DockerImages/metrics/prometheus.yml /etc/prometheus/prometheus.yml
ADD ./DockerImages/metrics/django.rules /etc/prometheus/django.rules

# Consoles can be found in localhost:9090/consoles/summary.html
ADD ./DockerImages/metrics/consoles/summary.html  /usr/share/prometheus/consoles/

ENTRYPOINT []

# Strangely, replacing the entrypoint doesn't properly work. Deleting it and adding everything as CMD does the trick
CMD /bin/prometheus -config.file=/etc/prometheus/prometheus.yml -storage.local.path=/prometheus -web.console.libraries=/usr/share/prometheus/console_libraries -web.console.templates=/usr/share/prometheus/consoles -storage.local.retention=6h