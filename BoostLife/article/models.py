from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented ID field
    name = models.CharField(max_length=100)  # Name of the image
    image = models.ImageField(upload_to='images/')  # Image file field
    status = models.BooleanField(default=True)  # Status field (True/False)
    created_date = models.DateTimeField(auto_now_add=True)  # Created date field (auto-populated)

    def __str__(self):
        return self.name
