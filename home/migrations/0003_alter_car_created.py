# Generated by Django 4.2.3 on 2023-07-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
    ]