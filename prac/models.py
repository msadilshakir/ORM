from django.db import models

# Create your models here.

class order(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password= models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class transaction(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    order_id = models.IntegerField(null=True)
