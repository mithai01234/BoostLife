from django.db import models

# Create your models here.
class Partner(models.Model):
    partner_id = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='partner_logos/')
    name = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    status = models.BooleanField(default=True)  # Add this field

    def __str__(self):
        return f"{self.name} - {self.store_name}"

class Package(models.Model):
    name = models.CharField(max_length=255)
    package_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)  # Optional field for additional details

    def __str__(self):
        return self.name

class Store(models.Model):
	name = models.CharField(max_length=255)
	newimage = models.FileField(upload_to='store_images/')
	address = models.TextField(blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	url = models.URLField(max_length=200, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	status=models.BooleanField(default=True)
	def __str__(self):
		return self.name
