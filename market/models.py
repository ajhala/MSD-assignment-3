from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class ExtUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    user_cell_phone = models.CharField(max_length=50, default='', null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ', blank=True, null=True,)
    state = models.CharField(max_length=50, default=' ', blank=True)
    zipcode = models.CharField(max_length=10, default='00000', blank=True)


class Produce(models.Model):
    user = models.ForeignKey(ExtUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Seller')
    produce_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=200)
    qty = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produce_name
