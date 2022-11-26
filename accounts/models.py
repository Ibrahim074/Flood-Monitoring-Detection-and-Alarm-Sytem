from django.db import models
from django.contrib.auth.models import AbstractUser

class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'

class Levels(models.TextChoices):
    LEVEL_1 = '1', '1'
    LEVEL_2 = '2', '2'
    LEVEL_3 = '3', '3'

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=8, choices=Gender.choices, default=Gender.MALE)
    access_levels = models.CharField(max_length=5, choices=Levels.choices, default=Levels.LEVEL_1)

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class HomeLocation(models.Model):
    home_address = models.CharField(max_length=500)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self)-> str:
        return self.home_address