# Generated by Django 3.0.1 on 2020-03-08 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200307_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='certifications',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stream',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='workexperience',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='date',
            field=models.DateField(default=datetime.date(2020, 3, 8)),
        ),
    ]
