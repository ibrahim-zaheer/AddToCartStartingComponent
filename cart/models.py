from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.TextField(null = True)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
    
class Cartitem(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    products = models.ForeignKey(Products,on_delete = models.CASCADE)    
    quantity = models.PositiveIntegerField(default = 0)
    date_added  = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'{self.products.name} X {self.quantity}'
    
