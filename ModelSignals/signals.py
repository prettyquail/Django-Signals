from .models import Buyer, Car, Order, Sale
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, m2m_changed, pre_delete
from django.contrib.auth.models import User
import uuid

# Create your models here.


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print("sender", sender)
    print("instance", instance)
    print("created", created)

    if created:
        Buyer.objects.create(user=instance)

# automatic code generated of a car
@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]


# When you delete code of car ,then save it. The buyer from_signal will set to "True"
@receiver(pre_save, sender=Car)
def pre_save_modify_buyer(sender, instance, **kwargs):
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()


# After saving car object, it will modify buyer from_signal to "true"
# and if the car code is not provided , then create code after saving and then resaving it
# @receiver(post_save, sender=Car)
# def post_save_modify_buyer_and_create_code(sender, instance, **kwargs):
#     if instance.code == "":
#         instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
#         instance.save()
#
#     obj = Buyer.objects.get(user=instance.buyer.user)
#     obj.from_signal = True
#     obj.save()

# if many to many field of Order i.e "Cars" gets changed, then this signal occures.
@receiver(m2m_changed, sender=Order.cars.through)
def m2m_changed_cars_order(sender, instance, action, **kwargs):
    total = 0
    total_price = 0

    # It is printing two times
    print(action)

    if action == "post_add" or action == "post_remove":
        print("running")
        print(action)
        for car in instance.cars.all():
            total += 1
            total_price += car.price
        instance.total = total
        instance.total_price = total_price
        instance.save()

# if order's models, total price field or active=True gets changed then the price in sales models also gets changed.
@receiver(post_save, sender=Order)
def post_save_create_or_update_sale(sender, instance, created, **kwargs):
    obj, _ = Sale.objects.get_or_create(order=instance)
    print("POST SALE")
    obj.amount = instance.total_price
    obj.save()


# The Order will be no longer active, after deleting Sale's object
@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, **kwargs):
    obj = instance.order
    obj.active = False
    obj.save()
