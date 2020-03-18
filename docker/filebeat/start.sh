#!/bin/bash

curl -XPUT 'http://elk:9200/template/filebeat?pretty' -d@/etc/filebeat/filebeat.template.json
/etc/init.d/filebeat start
nginx
tail -f /var/log/portfolio.log
