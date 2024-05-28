# Ramailo Ecommerce

## Get Started

### 1. Prerequisites

- [Django](https://www.djangoproject.com/) - Python framework for full stack applications
- [Postgres](https://www.postgresql.org/) - Relational database management system (RDBMS)
- [DRF](https://www.django-rest-framework.org/) - Django rest framework for building web apis

### 2. Installation

On the command prompt run the following commands:

``` 
 $ git clone https://github.com/dhamaladev/ecommerce-backend.git
 $ cd ecommerce-backend
 ```
 # For Backend
```
 $ cd backend
 $ virtualenv myenv (setup virtual environment for your backend application)
 $ cd myenv 
 $ Scripts/activate (virtual env gets activated)
 $ cd ..
 $ pip install -r requirements.txt

 ```
 
 ```
 - Now insert your db data into .env file in the root project with names mentioned.
 ```
 ```
 $ python manage.py makemigrations
 $ python manage.py migrate (Now whenever is runserver run data gets inserted into the database)
$ python manage.py runserver (This will run the server and you can look it on http://localhost:8080/)