# Generated by Django 4.0.1 on 2022-04-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0016_meal_one_meal_per_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(choices=[('LU', 'Lunch'), ('DI', 'Dinner')], default='LU', max_length=2),
        ),
    ]
