from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, null=True, blank=False)
    image_url = models.CharField(null=True, blank=False)

    def __str__(self):
        return self.product_name
