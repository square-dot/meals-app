# Generated by Django 4.0.1 on 2022-02-04 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_meal_mealtype_alter_commensal_creation_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commensal',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 0, 16, 23, 623289), verbose_name='creation time'),
        ),
    ]
