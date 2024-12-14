from django.db import models
from app_modules.base.models import BaseModel
from app_modules.products.models import Products
from django.contrib.auth import get_user_model

user = get_user_model()
# Create your models here.

class Order(BaseModel):
    customer = models.ForeignKey(user,related_name="order_customer",on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.id

class OrderItems(BaseModel):
    order = models.ForeignKey(Order,related_name="order",on_delete=models.CASCADE)
    product = models.ForeignKey(Products,related_name="order_product",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.id