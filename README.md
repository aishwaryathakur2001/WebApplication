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

#### A development server

Run this command:

```
python manage.py runserver
```


