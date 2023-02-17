# Rishat

shop...

## Global Requirements

1. Debian-like system
2. Python 3.10
3. Pip
4. Postgres

## Pre-Installation

1. Configure postgres (create new user and database, for
   example https://losst.pro/ustanovka-postgresql-ubuntu-16-04?ysclid=lctjuo3nn2800527354)

## Installation

1. Open terminal and change directory to **/opt**.
2. Run "git clone https://github.com/gpapaskiri/rishat.git". In opt will appear folder **rishat**.
3. Change owner for folder to user with sudoers (for example, **sudo chown username. -R webtronics**).
4. Move to directory rishat and run **pip install -r requirements.txt**.
5. In **settings.py** change settings for connecting to database in section **database** and allow hosts in section **
   ALLOWD_HOSTS**.
6. Run **python3 manage.py makemigrations** and **python3 manage.py migrate**. It will create all tables and relations.
7. Run **python3 manage.py createsuperuser** ande execute all suggested steps.
8. Run **python manage.py runserver 0.0.0.0:8000 --insecure**

## Usage

Api has 2 GET methods:

1. item/id - return information about product.
2. buy/id - create stripe session id and redirect to payment form.

## Run as service

Create in **/etc/systemd/system/** file **rishat.service** with next content:

[Unit]\
Description=Rishat app\
After=syslog.target\
After=network.target

[Service]
Type=simple\
User=root\
WorkingDirectory=/opt/rishat\
ExecStart=/usr/bin/python3 /opt/rishat/manage.py runserver 0.0.0.0:8000 --insecure\
RestartSec=5\
Restart=always

[Install]\
WantedBy=multi-user.target


