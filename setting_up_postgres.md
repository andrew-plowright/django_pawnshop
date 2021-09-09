1. Install `pip install psycopg2`
2. Create a Postgres database on the **localhost** server
3. In _Settings.py_:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘<db_name>’,
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }
}
```
4. Migrate:
```
py manage.py makemigrations
py manage.py migrate
```

5. Create a super user
```
py manage.py createsuperuser
```