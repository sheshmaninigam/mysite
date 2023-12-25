from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Addcar(models.Model):
    car_code = models.IntegerField(default=100,validators=[MinValueValidator(100)])
    car_person_name = models.CharField(default="ABC",max_length=100)
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_price = models.IntegerField(validators=[MinValueValidator(0)])
    car_desc = models.TextField()
    car_image = models.ImageField(default='car_image.jpg', upload_to='car_image')
    car_image1 = models.ImageField(default='car_image.jpg', upload_to='car_image1')
    car_image2 = models.ImageField(default='car_image.jpg', upload_to='car_image2')
    car_image3 = models.ImageField(default='car_image.jpg', upload_to='car_image3')
    car_image4 = models.ImageField(default='car_image.jpg', upload_to='car_image4')
    car_image5 = models.ImageField(default='car_image.jpg', upload_to='car_image5')

    def __str__(self):
        return self.car_person_name
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()



    def __str__(self):
        return self.first_name


