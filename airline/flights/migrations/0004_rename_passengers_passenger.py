# Generated by Django 3.2.4 on 2021-07-18 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
