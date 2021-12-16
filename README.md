# WebApplication
## Functionality

- Create an account 
- Registration
    - via username 
    - password
    - contact number
    - email
    - address
    - profile image
    
- Log in
    - via username & password
    
- Edit Profile
    - Change password
    - Change contact number
    - Change email
    - Change address
    - Change profile image

- Log out


## Installations and Setup

### Install pip

```
python -m pip install -U pip
```

### Install virtual environment

```
pip install virtualenv
```

### Create a virtual environment

```
virtualenv venv
```

### Activation of virtual environment

```
cd venv
cd Scripts 
activate
cd..
cd..
```
### Install Django

```
pip install django
```

### Create a Django project

```
django-admin startproject project_name
cd project_name
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `source/app/conf/development/settings.py` if you want to develop the project.

2. Edit `source/app/conf/production/settings.py` if you want to run the project in production.

### Apply migrations

```
python source/manage.py migrate
```

### Collect static files (only on a production server)

```
python source/manage.py collectstatic
```

### Running

#### Start the server

Run this command:

```
python manage.py runserver
```

How to access URLs

Copy `http://127.0.0.1:8000/` url and paste it on website

Ways to access different pages: 

http://127.0.0.1:8000/index.html     -> This will take you to home page
http://127.0.0.1:8000/register.html  -> This will take you to user registration page
http://127.0.0.1:8000/Login.html  -> This will take you to user login page

