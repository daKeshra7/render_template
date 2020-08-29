from django.db import models

# Create your models here.
class product_info(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places= 2, max_digits=1000)
    comment = models.TextField(default="Enter your text here", blank=False, null=False)
    