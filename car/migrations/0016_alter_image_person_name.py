# Generated by Django 4.2.5 on 2023-11-03 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0015_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='person_name',
            field=models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='car.addcar'),
        ),
    ]