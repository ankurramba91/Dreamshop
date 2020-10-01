from django.db import models

# Create your models here.


class Product(models.Model):
   
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title + "---" + self.category


# checkout models

class Contact(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.TextField()
    total = models.CharField(max_length=200)

    def __str__(self): #this is used to show name in admin contact
        return self.name+"---"+self.email