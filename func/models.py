from django.db import models

# Create your models here.
class people(models.Model):
    firstname = models.CharField(max_length=10000)
    lastname = models.CharField(max_length=10000)
    email = models.CharField(max_length=10000)
    value = models.CharField(max_length=100000)


class comic(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    image = models.CharField(max_length=1000)

