from django.db import models
from django.contrib.auth.models import User
# Create your models here.




FLAG_TYPE = (
    ('New', 'New'),
    ('Sale', 'Sale'),
    ('Feature', 'Feature'),
)





class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    flag = models.CharField(max_length=20,choices=FLAG_TYPE)
    
    
    def __str__(self):
        return self.name