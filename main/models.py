import uuid  # Add this import
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Add this line
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
