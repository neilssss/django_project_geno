from django.db import models

# Create your models here.
class Members(models.Model):
    first = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Fish(models.Model):
    fish_type = models.CharField(max_length=225)
    fish_name = models.CharField(max_length=225)
    fish_size = models.FloatField()
    fish_price = models.FloatField()
