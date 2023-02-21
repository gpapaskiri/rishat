# Rishat

shop...

## Global Requirements

1. Debian-like system
2. Python 3.10, python3.10-env
3. Postgres
4. Nginx

## Pre-Installation

1. Configure postgres (create new user and database, for
   example https://losst.pro/ustanovka-postgresql-ubuntu-16-04?ysclid=lctjuo3nn2800527354)

## Installation

1. Open terminal and change directory to **/opt**.
2. Run "git clone https://github.com/gpapaskiri/rishat.git". In opt will appear folder **rishat**.
3. Change owner for folder to user with sudoers (for example, **"sudo chown username. -R rishat"**).
4. Move to directory rishat and create virtual env, by using command **"python3 -m venv venv"**.
5. Activate virual env **"source venv/bin/activate** and install requirements **"pip3 install -r requirements.txt"**.

## Preconfig

1. In **.env** change set your own settings. Located in the same folder as settings.py.
2. Create all table and relationship **python3 manage.py makemigrations** and **python3 manage.py migrate**.
3. Create user for django-admin **python3 manage.py createsuperuser**.
4. Collect static files **"python3 manage.py collectstatic"**.

## Run server

1. In **/etc/systemd/system/** create 2 files **"gunicorn.socket"** and **"gunicorn.servcice"**.
2. Run **"sudo systemctl start gunicorn.socket"** and **"sudo systemctl start gunicorn.service"**.
3. In **/etc/nginx/sites-available/** create file **rishat**.
4. Create symlink **"sudo ln -s /etc/nginx/sites-available/rishat /etc/nginx/sites-enabled/"**.
5. Run **"sudo systemctl start nginx"**.

Now server is available on **"http://server_ip"**

## Usage

Api has 2 GET methods:

1. item/id - return information about product.
2. buy/id - create stripe session id and redirect to payment form.
