# Generated by Django 4.2.1 on 2023-05-18 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='wallet_adress',
            new_name='vallet_adress',
        ),
    ]
