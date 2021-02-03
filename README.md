# blood-donation
Blood donation 

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
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
