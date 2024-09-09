from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Item name
    price = models.IntegerField()  # Item price
    description = models.TextField()  # Item description
    
    def __str__(self):
        return self.name