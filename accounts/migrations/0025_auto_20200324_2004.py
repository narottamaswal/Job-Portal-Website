# Generated by Django 3.0.1 on 2020-03-24 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20200319_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='date',
            field=models.DateField(default=datetime.date(2020, 3, 24)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='jobtitle',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='skills',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='saved',
            name='Jobtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
