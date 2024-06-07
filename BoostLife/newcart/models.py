from django.db import models

# Create your models here.
class DeliveryCharge(models.Model):
    id = models.AutoField(primary_key=True)
    charge =  models.IntegerField()
    status= models.BooleanField(default=True)

from django.db import models
from registration.models import CustomUser
from product.models import Product

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    u_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    status = models.CharField(max_length=20, default='Active')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart item - ID: {self.id}"

class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    openingstock=models.IntegerField(default=0)
    item_id=models.ForeignKey(Product,on_delete=models.CASCADE)
  #  pro_id= models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)