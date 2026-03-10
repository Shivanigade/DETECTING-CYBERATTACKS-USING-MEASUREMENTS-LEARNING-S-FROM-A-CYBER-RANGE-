from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class detecting_cyber_attacks(models.Model):

    rid= models.CharField(max_length=300)
    datetime= models.CharField(max_length=300)
    host= models.CharField(max_length=300)
    src= models.CharField(max_length=300)
    proto= models.CharField(max_length=300)
    type= models.CharField(max_length=300)
    spt= models.CharField(max_length=300)
    dpt= models.CharField(max_length=300)
    srcstr= models.CharField(max_length=300)
    cc= models.CharField(max_length=300)
    country= models.CharField(max_length=300)
    locale= models.CharField(max_length=300)
    latitude= models.CharField(max_length=300)
    longitude= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



