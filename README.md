# Installation #

Follow these steps to get the application running in your local/test environment:

## Requirements ##
* Python 3.8 and above
* PostgreSQL and above (Install `postgresql-contrib` and `pgadmin4` alongside)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

## db setup ##
```
* Create .env file as same .env.exmaple format and provide your credentials in .env file
* Also change this credentials in the docker-compose file where it's needed
```
## Run project by the following commands ## 
```
docker-compose up --build
```

## API document link ##
```
http://127.0.0.1:8000/api/swagger-ui/
```

## Postman collection ##
```
*As per your requirement i've added postman collection for you, Please find it with the name 
'AccuKnox.postman_collection.json' 
```


