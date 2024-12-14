from django.db import models
from app_modules.base.models import BaseModel
# Create your models here.

class Products(BaseModel):
    name = models.CharField(max_length=512)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    decription = models.TextField(blank=True,null=True)

class ProductImages(BaseModel):
    product = models.ForeignKey(Products,related_name="product_images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")