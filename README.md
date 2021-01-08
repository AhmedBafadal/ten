#Ten Test

## To Build
```
1.
docker build .

2.
docker-compose build
```

## To Run
```
1. Create superuser
docker-compose run app sh -c "python manage.py createsuperuser"

2.
docker-compose up
```

Please access /members endpoint to upload member csv, and /inventory to upload inventory csv. access to "0.0.0.0:8000/admin/" with the user details to submit from the createsuperuser step.

endpoint api could not be completed due to illness.