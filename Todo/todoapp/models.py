from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=1,max_digits=10)

    def __str__(self):
        return self.name