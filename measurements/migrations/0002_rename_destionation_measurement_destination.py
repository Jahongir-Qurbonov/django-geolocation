# Generated by Django 4.1.1 on 2022-09-06 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='destionation',
            new_name='destination',
        ),
    ]