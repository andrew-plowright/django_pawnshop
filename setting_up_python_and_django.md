# Initial set up

Main source of info:
https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter


1. Downloaded latest version of Pycharm (2021.2.1)

2. Downloaded latest version of Python (3.9) and installed it here

```
C:/Users/Andrew/AppData/Local/Programs/Python/Python39/
```
**NOTE**: the `PATH` environment variable must be set up when installing Python39. Or maybe not? I don't know.


3. Created a virtual environment (called `venv` by going to project folder and running `virtualenv` (which is on `PATH`)

```
cd C:\Users\Andrew\Dropbox\Scripts\ScratchTests\LearnDjango
virtualenv venv

```

4. Set this virtual environment as the "interpreter" in the PyCharm project. You can then use commands like `django-admin` from the **Terminal** inside Pycharm

5. From within the virtual environment, you can run this to install all the packages required:

```
pip install -r requirements.txt
```

6. From within the `...\LearnDjango\` folder, run:
```
django-admin startproject mytestite
```

7. Then go to the newly created `mytestsite` folder and run (from the terminal inside Pycharm):
```
py manage.py runserver
```

This can then be terminated using `Ctrl+C` (aka: `Ctrl+BREAK`)


8. Now open this address in the browser to see if it worked: `http://127.0.0.1:8000/`

# Creating a super user

**NOTE**: this applies to the database. If you're using Postgres, you need to make the Postgres database first
```
py manage.py createsuperuser
```

Temporary username: **andrew_super**

Temporary passsword: **capybara**

# Creating normal user

This guys has permissions:

Username: **rodrigo**

Password: **chopchop22**

This guy doesn't:

Username: **gustave**

Password: **chipchip22**

# Extra packages

### Django extensions (for shell_plus)

Install:
```
pip install django-extensions
pip install ipython
```

Add under `INSTALLED_APPS` in **settings.py**

```
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

### Django debug toolbar

Install:
```
pip install django-debug-toolbar
```

Under **settings.py**:
```
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

INTERNAL_IPS = [
    '127.0.0.1',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}
```

Under **urls.py**
```
import debug_toolbar

urlpatterns = [
    ...
    path('__debug__/', include(debug_toolbar.urls)),
]
```