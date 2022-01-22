from django.db import models

# Create your models here.
class trains(models.Model):
    train_name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    price=models.FloatField(default=120)
    seats_available=models.IntegerField()

class person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    date_and_time_of_booking=models.DateTimeField(auto_now_add=True)
    train=models.ForeignKey('trains', on_delete=models.CASCADE)