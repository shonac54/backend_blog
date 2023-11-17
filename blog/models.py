from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    name = models.CharField(default='', max_length=100)
    profile = models.CharField(default='', max_length=500)
    email = models.CharField(default='', max_length=100)
    password = models.CharField(default='', max_length=100)

class BlogModel(models.Model):
    userid = models.CharField(default='', max_length=100)
    title =  models.CharField(default='', max_length=100)
    message = models.CharField(default='', max_length=100)