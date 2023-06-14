
from django.db import models
import time

from django.db.models.signals import *
from django.dispatch import receiver



class Chitfund (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    email = models.EmailField()
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    chitfund_emp = models.ManyToManyField(Chitfund,related_name="addresses")




@receiver(pre_save, sender=Chitfund)
def pre_save (sender, instance, **kwargs):
    print("Your chitfund account will be saved don't worry.......!!!!!")

    time.sleep(10)

@receiver(post_save,sender = Chitfund)
def post_save (sender,instance,created,**kwargs):
    print('Your chitfund account saved successfully.......!!!!!')

@receiver(pre_delete,sender = Chitfund)
def pre_delete (sender,instance,**kwargs):
    print('OOOOPS......Your chitfund account will be deleted .......!!!!!')

    time.sleep(20)

@receiver(post_delete,sender = Chitfund)
def post_delete (sender,**kwargs):
    print('SORRYYYYY......Your chitfund account deleted .......!!!!!')


@receiver(m2m_changed, sender=Address.chitfund_emp.through)
def m2m_changed (sender, instance, action, reverse, model, pk_set, **kwargs):
    print('m2m action working....!!!!')

'''

from djsignalling.models import *
chitfund_employee1 = Chitfund(id = 501 , name = 'akshay',address = 'satara',age = 26,email = 'akshay@gmail.com',balance = 7000000)
chitfund_employee1.save()

chitfund_employee2 = Chitfund(id = 502 , name = 'anisha',address = 'satara',age = 21,email = 'anisha@gmail.com',balance = 100000)
chitfund_employee2.save()

chitfund_employee3 = Chitfund(id = 503 , name = 'anjali',address = 'satara',age = 19,email = 'anjali@gmail.com',balance = 8000000)
chitfund_employee3.save()

chitfund_employee4 = Chitfund(id = 504 , name = 'omakar',address = 'satara',age = 24,email = 'omkar@gmail.com',balance = 100000)
chitfund_employee4.save()

'''