# Generated by Django 4.0.1 on 2022-02-02 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commensal',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name='creation time'),
        ),
        migrations.AddField(
            model_name='commensal',
            name='family_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='commensal',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
