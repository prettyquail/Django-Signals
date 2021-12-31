from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"

    # Overriding save method
    # def save(self, *args, **kwargs):
    #     if self.code == "":
    #         self.code = str(uuid.uuid4()).replace("-","").upper()[:10]
    #     return super().save(*args,**kwargs)


class Order(models.Model):
    name = models.CharField(max_length=200)
    cars = models.ManyToManyField(Car)
    total = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.amount)
