# Generated by Django 4.2.5 on 2023-11-03 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]