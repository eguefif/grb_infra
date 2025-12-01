start-services:
    docker stack deploy -c docker-compose.yml --with-registry-auth grb

stop-services:
    docker stack rm grb

update-alertsys:
    docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:alertsys-latest alertsys

update-backend:
    docker service update --update-delay=10s --with-registry-auth --image eguefif/grb-amateur:backend-latest backend
