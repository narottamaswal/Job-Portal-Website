# Generated by Django 3.0.1 on 2020-03-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200307_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='maxexp',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='minexp',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
