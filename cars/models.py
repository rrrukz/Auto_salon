from lib2to3.fixer_util import BlankLine

from django.db import models
from django.contrib.auth.models import User

# models.py

from django.db import models

class Avto(models.Model):

    AVTO_MARK=(
        ('chevrolet','CHEVROLET'),
        ('lada','LADA'),
        ('porsche','PORSCHE'),
        ('nissan','NISSAN'),
        ('bugatti','BUGATTI'),
        ('lamborgini','LAMBORGINI'),
        ('audi','AUDI'),
        ('mercedes','MERCEDES'),
        ('bmw','BMW'),
        ('toyota','TOYOTA'),
    )
    AVTO_MODEL= (
        ('sedan', 'SEDAN'),
        ('suv', 'SUV'),
        ('hatchback', 'HATCHBACK'),
        ('pick-up truck', 'PICK-UP TRUCK'),
        ('crossover', 'CROSSOVER'),
        ('coupes', 'COUPES'),
        ('convertible', 'CONVERTIBLE'),
        ('van', 'VAN'),
        ('bmw', 'BMW'),
        ('toyota', 'TOYOTA'),
    )
    avto_mark=models.CharField(
        max_length=250,
        choices=AVTO_MARK,
        default="chevrolet",
        verbose_name="MARC OF THE VEHICLE"
    )
    avto_model=models.CharField(
        max_length=240,
        choices=AVTO_MODEL,
        default="sedan",
        verbose_name="MODEL OF THE VEHICLE"
    )

    name=models.CharField(max_length=250,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Cars/',null=True,blank=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)  # Quantity of cars
    rating = models.PositiveIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=0)  # Star rating
    year=models.PositiveIntegerField(default=1)
    mileage=models.PositiveIntegerField(default=0)
    transmission=models.CharField(max_length=100,null=True,blank=True)
    fuel_type=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.avto_mark} {self.name}-({self.price}$)"

