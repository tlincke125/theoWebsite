from django.db import models

from datetime import date
# Create your models here.


class Post(models.Model):
    #For the future, use auto_now_add=True - makes a single instance of date on creation
    #default=date.today is the same, but defaults to the creating day
    date = models.DateField(default=date.today)

    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length = 200)

    #textfield doesn't restrict databse level, use charField for that, not necessary though
    introContent = models.TextField(max_length=500)
    #max length defaults to 50

    idVal = models.SlugField()
    category = models.SlugField()

    pictureID = models.CharField(max_length=50)

    featured = models.BooleanField(default = False)
    recent1 = models.BooleanField( default = False)
    recent2 = models.BooleanField( default = False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=20)

    content = models.TextField(max_length=200)

    idVal = models.SlugField()
    category = models.SlugField()

    def __str__(self):
        return self.name + ":" + self.category + ":" + self.idVal
