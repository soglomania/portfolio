# TODO

* Change the docker base image to alpine
* use docker compose to create different services
    database service (Postgresql)
        create a volume to map the container db data to the host file system
    
    /logs
        logs service
        use syslog to collect logs and store them
        create an endpoint /log to visualize the logs in the browser in realtime
    /metrics  
        prometheus to collect some application metrics and display the metrics consoles in the ui

    /metrics-graph
        graphana container image to visualize the metrics 

* Play with the django test lib and implement some test in the application (UI,....)



