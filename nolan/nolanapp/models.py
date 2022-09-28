 
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=60)
    desc = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to = "static/prod_image" ,null=True,blank=True)
    
    def __str__(self):
        return self.name
    