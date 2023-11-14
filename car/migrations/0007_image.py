# Generated by Django 4.2.5 on 2023-11-03 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0006_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(default='car_image.jpg', upload_to='car_image')),
                ('car_image1', models.ImageField(default='car_image.jpg', upload_to='car_image1')),
                ('car_image2', models.ImageField(default='car_image.jpg', upload_to='car_image2')),
                ('car_image3', models.ImageField(default='car_image.jpg', upload_to='car_image3')),
                ('car_image4', models.ImageField(default='car_image.jpg', upload_to='car_image4')),
                ('car_image5', models.ImageField(default='car_image.jpg', upload_to='car_image5')),
                ('car_person_name', models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
