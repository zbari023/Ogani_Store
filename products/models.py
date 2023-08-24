from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    
    
    def __str__(self):
        return self.name