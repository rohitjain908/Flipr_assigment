# Generated by Django 3.1.8 on 2021-11-13 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resturant',
            name='rating',
        ),
    ]
