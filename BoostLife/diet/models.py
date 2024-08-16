from django.db import models

# Create your models here.
from django.db import models

class Diet(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    carbs = models.BooleanField(default=False)
    protein = models.BooleanField(default=False)
    fat = models.BooleanField(default=False)
    number_of_intake = models.CharField(max_length=255)
    image = models.ImageField(upload_to='diet_images/')
    level= models.CharField(max_length=255)
    def __str__(self):
        return self.name
class TimeofFood(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='timeoffood_images/')
    number_of_cup = models.CharField(max_length=50)
    number_of_gram = models.CharField(max_length=50)
    calories = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    diet_id = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DietVideo(models.Model):
    id = models.AutoField(primary_key=True)
    preptime = models.CharField(max_length=50)
    carbs = models.CharField(max_length=50)
    fat = models.CharField(max_length=50)
    protein = models.CharField(max_length=50)
    video = models.FileField(upload_to='diet_videos/')
    precautions = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)
    timeoffood_id = models.ForeignKey(TimeofFood, unique=True,on_delete=models.CASCADE, null=True, blank=True)
    video_url = models.CharField(max_length=800, blank=True)
    type = models.CharField(max_length=8, blank=True)
    def __str__(self):
        return f"Diet Video {self.id}"

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    measurement = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ingredient_images/')
    timeoffood_id = models.ForeignKey(TimeofFood, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
