from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.db import models
class Catagory(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    status= models.BooleanField(default=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    status= models.BooleanField(default=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=100)
    cat_name = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    status= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item_old_price = models.FloatField()
    discount = models.IntegerField()
    item_new_price = models.FloatField()
    most_popular=models.BooleanField(default=False)
    recommended=models.BooleanField(default=False)
    goal=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name

