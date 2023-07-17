# Generated by Django 4.0 on 2022-01-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_alter_food_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('drinks', 'Drinks')], default='drinks', max_length=9),
        ),
    ]