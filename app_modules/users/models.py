from django.db import models
from app_modules.base.models import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):

    ADMIN    = "Admin"
    CUSTOMER = "Customer"

    TYPE_CHOICES = (
        (ADMIN,ADMIN),
        (CUSTOMER,CUSTOMER)
    )

    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"
    email          = models.EmailField(unique=True,max_length=512)
    username       = models.CharField(blank=True,null=True,max_length=512)
    type           = models.CharField(choices=TYPE_CHOICES,max_length=20,default=CUSTOMER)

    def __str__(self):
        return self.get_full_name()