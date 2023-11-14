from django import forms
from car.models import Addcar

class Addcar_Form(forms.ModelForm):
    class Meta:
        model = Addcar
        fields = ["car_code","car_person_name","car_name","car_model","car_price","car_desc","car_image",
                  "car_image1","car_image2","car_image3","car_image4","car_image5"]
        


        