# Blood-Donation
Django village blood donation web apps 

> The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the apps on Windows, you should have little problem getting up and running.

### Setup

- Python 3.8
- Django 3.0.1

1st open your terminal than follow the command.
```base
git clone https://github.com/mbrsagor/blood-donation.git
cd blood-donation
virtualenv venv --python=python3.8
source venv/bin/activate
```
Then create `.env` file and paste code from `.env-sample` file which has basically project some inforamtions for production and development purpose.
```base
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

###### If you want to run the project docker pls follow the below command:
```bash
docker-compose.yml
```

##### Django database configuration example:
```python
# settings.py
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost', # Here your database host
        'PORT': 5432, # Database port
    }
}

```
