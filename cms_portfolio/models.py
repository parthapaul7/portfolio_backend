from django.db import models
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type= models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)
