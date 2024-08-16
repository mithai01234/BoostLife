from django.db import models

class Workout(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    cal = models.CharField(max_length=50)
    num_exercise = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    status= models.BooleanField(default=True)
    banner=models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    video_url = models.CharField(max_length=800,blank=True)
    type=  models.CharField(max_length=8,blank=True)
    time = models.CharField(max_length=50)
    repetition_time = models.CharField(max_length=50)
    status= models.BooleanField(default=True)
    recommended=models.BooleanField(default=False)

    def __str__(self):
        return self.name
class WorkOutBanner(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=1000)
    add_photo = models.ImageField(upload_to='add_photos/')
    status= models.BooleanField(default=True)
    level = models.CharField(max_length=500,default=None)
    workout_id=models.CharField(max_length=500,blank=True, null=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Item ID: {self.id}"