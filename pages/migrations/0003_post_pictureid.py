# Generated by Django 2.1.5 on 2019-02-11 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190211_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pictureID',
            field=models.CharField(default='images/hi.jpg', max_length=50),
            preserve_default=False,
        ),
    ]