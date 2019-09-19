# notification-service

This project is one of the microservices of web project. 
For handling notifications like text message,emails,push etc.
Pluggable with other django projects.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development 
and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

    sudo apt install virtualenv
    virtualenv -p python3.5 {envname} && cd {envname}
    source bin/activate
    cd notfication-service
    pip install -r docs/requirements.txt
    
#### Database Configuration 

In *postgres* console
      
    CREATE DATABASE pms_notifications;
    GRANT ALL PRIVILEGES ON DATABASE pms_notifications TO postgres;
    
Make migrations for app and django in root of project
    
    python manage.py makemigrations
    python manage.py makemigrations {appname} #api here
    python manage.py migrate
    python manage.py runserver

## Running the tests

We can run automated tests by 

    python manage.py test

## Deployment

  Deployment instructions 
 
## Built With

[Django Web Framework](https://docs.djangoproject.com/en/2.2/)

## Versions

