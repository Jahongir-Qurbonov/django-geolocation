# Generated by Django 4.1.1 on 2022-09-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, verbose_name='location')),
                ('destionation', models.CharField(max_length=200, verbose_name='destionation')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='distance')),
                ('created', models.DateField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'measurement',
                'verbose_name_plural': 'measurements',
            },
        ),
    ]