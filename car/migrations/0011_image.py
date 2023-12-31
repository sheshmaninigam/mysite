# Generated by Django 4.2.5 on 2023-11-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('images', models.ImageField(default='car_image.sjpg', upload_to='car_images')),
                ('images1', models.ImageField(default='car_images.jpg', upload_to='car_images1')),
                ('images2', models.ImageField(default='car_images.jpg', upload_to='car_images2')),
                ('images3', models.ImageField(default='car_images.jpg', upload_to='car_images3')),
                ('images4', models.ImageField(default='car_images.jpg', upload_to='car_images4')),
                ('images5', models.ImageField(default='car_images.jpg', upload_to='car_images5')),
            ],
        ),
    ]
