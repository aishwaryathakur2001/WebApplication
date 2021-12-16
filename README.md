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


## Installing

### Clone the project

```
git clone https://github.com/egorsmkv/simple-django-login-and-register
cd simple-django-login-and-register
```

### Install dependencies & activate virtualenv

```
pip install pipenv

pipenv install
pipenv shell
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
