# Generated by Django 4.0.1 on 2022-03-15 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0014_alter_meal_commensal_alter_meal_meal_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='commensal',
            new_name='user',
        ),
    ]
