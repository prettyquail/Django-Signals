from django.contrib import admin
from .models import Buyer, Car, Order, Sale

# Register your models here.


admin.site.register(Buyer)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Sale)
