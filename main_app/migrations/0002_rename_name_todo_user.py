# Generated by Django 4.2 on 2023-04-26 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='user',
        ),
    ]
