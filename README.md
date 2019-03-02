# Theo's Website
This is my personal website for displaying my projects and ideas at school. This version is currently ** not ** the most updated version. I have recently switched to the Django framework so all of my previous firebase stuff is being hosted at theolincke.com, but this is the most recent. I plan to deploy my webpage within the next week. Currently, Django is set on debug = True, so the steps to take to deploy the website will be to find a provider (Heroku) and deploy on  production mode. There are just a few kinks I need to work out such as adding test deploy cases and adding some new blog posts that I have been working on. Otherwise, this will make my website a lot easier to edit and fix. In the future, it will also add more functionality.

## Structure
Django needs to be installed. I used virtualenv for python to install dependencies in a workspace rather than directly to my native python install.

```bash
$ sudo apt-get install virtualenv
$ virtualenv -p python3 <venv>
$ source ./venv/bin/activate
$ pip install <dependencies>
$ pip install django
```

The django file structure is as follows:

### Main directory <theoWebsite>
This is the project name it contains everything, in it is the database:
In my case, I'm using sqlite, but I think I'll switch to postgresql because sqlite isn't the best database to know in production (for my app, I'm not storing much at all other than comments so I don't really need a robust database, I would only switch for learning purposes). manage.py is the powerhouse of the app, run this script with different system arguments. To see what you can do with manage.py run

```bash
$ python manage.py help
or just
$ python manage.py
```

Some usefull commands are:
```bash
$ python manage.py runserver
Runs a local host on port 8000
$ python manage.py migrate <model to migrate>
$ python manage.py makemigrations
Updates database values
$ python manage.py createsuperuser
Creates superuser. You need my authentication to change this so not much use for this project, but helps for your own project
```

### Pages
This is my app project. You need to create an app for this folder to show up. In this folder, I have admin.py (edit this to show which models show up on your admin page), apps.py (the folder to import in settings) models.py (a description of the object oriented models to be stored in the database), tests.py (a script to test your website) urls.py (had to make this, creates url paths for app) and views.py (http response for each url).

### templates
This contains the html templates using jinja 2 for static webpage rendering based on the arguments provided in ./pages/views.py

### theoWebsite
This contains the information about the project as a whole such as settings (something you'll be editing a lot), urls.py (for this, all you really  need to do is include urls  from your app directory).

## Summary
I've described the rough directory structure for my app, however, I got all of this from the [django documentation](https://docs.djangoproject.com/en/2.1/ "django's  documentation") Django is really good at documenting everything and describing how to run a django app, so have a read if you're interested. I hope  you enjoy.
