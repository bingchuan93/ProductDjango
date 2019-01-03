from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField(blank=True, null=False)
    price           = models.DecimalField(decimal_places=2, max_digits=100)
    summary         = models.TextField(blank=True)
    featured        = models.BooleanField(null=True)

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        return reverse("products:product_details", kwargs={'id': self.id})