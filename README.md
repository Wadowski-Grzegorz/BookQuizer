# BookQuizer

Uruchomienie przez docker compose up.

Najpierw baza danych nie chciała się uruchomić - nie tworzyła się baza `bookdb`.  
Zrobiłem to ręcznie:

```bash
docker exec -it <id_kontenera> psql -U postgres
CREATE DATABASE bookdb;
