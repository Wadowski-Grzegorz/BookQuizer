# BookQuizer

login-service to pozostałość, nie jest używana.
Z tego też powodu w docker-compose.yml ta część jest zakomentowana.

Najpierw baza danych nie chciała się uruchomić - nie tworzyła się baza bookdb.
Zrobiłem to ręcznie:
>docker exec -it <id_kontenera>  psql -U postgres
>CREATE DATABASE bookdb;
