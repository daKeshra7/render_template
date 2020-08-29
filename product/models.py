from django.db import models

# Create your models here.

class Products(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    height = models.DecimalField(decimal_places=2, max_digits=10000)
    about_you = models.TextField(default="Not more than 250 characters", max_length=250)
    photo = models.ImageField(max_length=255,upload_to='pictures')
    
    #featured = models.BooleanField(blank=False)


