from django.db import models

# Create your models here.


class Addcar(models.Model):
    car_code = models.IntegerField(default=100)
    car_person_name = models.CharField(default="ABC",max_length=100)
    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_price = models.IntegerField()
    car_desc = models.TextField()
    car_image = models.CharField(
        max_length=500,
        default="https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg"
    )

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


