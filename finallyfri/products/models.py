from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False,
                                default="Art")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False,
                                blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
