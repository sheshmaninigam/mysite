# Generated by Django 4.2.5 on 2023-12-25 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0017_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='car_price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
