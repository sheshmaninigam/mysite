# Generated by Django 4.2.5 on 2023-11-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_addcar_car_image1_addcar_car_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcar',
            name='car_image1',
            field=models.ImageField(default='car_image.jpg', upload_to='car_image1'),
        ),
        migrations.AlterField(
            model_name='addcar',
            name='car_image2',
            field=models.ImageField(default='car_image.jpg', upload_to='car_image2'),
        ),
        migrations.AlterField(
            model_name='addcar',
            name='car_image3',
            field=models.ImageField(default='car_image.jpg', upload_to='car_image3'),
        ),
        migrations.AlterField(
            model_name='addcar',
            name='car_image4',
            field=models.ImageField(default='car_image.jpg', upload_to='car_image4'),
        ),
        migrations.AlterField(
            model_name='addcar',
            name='car_image5',
            field=models.ImageField(default='car_image.jpg', upload_to='car_image5'),
        ),
    ]
