from django.db import models

# Create your models here.

class Destination(models.Model):

    price = models.IntegerField(default=0)
    place = models.CharField(max_length=100,default='noPlace')
    description = models.TextField(default='none')
    photo = models.ImageField(upload_to='pics', default='none')
    offer = models.BooleanField(default=False)
