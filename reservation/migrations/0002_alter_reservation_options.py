# Generated by Django 4.2.3 on 2023-07-15 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('date', 'time')},
        ),
    ]