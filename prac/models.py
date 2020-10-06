from django.db import models

# Create your models here.

class order(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password= models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class transaction(models.Model):
    
    payment_type = models.CharField(max_length=30)
    transaction_status= models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    order_id = models.IntegerField(null=True)
