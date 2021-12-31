from django.db import models
from django.db.models.deletion import CASCADE

from django.contrib.auth.models import User
import os
from twilio.rest import Client

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    # slug=models.AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    slug=models.SlugField(max_length=50,null=True)
    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True)
    desc=models.TextField(default="")
    
    image=models.ImageField(upload_to='image')
    price=models.IntegerField(default='')
    date=models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.name


class Carousel(models.Model):
    image=models.ImageField(upload_to='image')

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name


class UserProduct(models.Model):
    user=models.ForeignKey(User,null=False,on_delete=CASCADE)
    product=models.ForeignKey(Product,null=False,on_delete=CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

# class Payment(models.Model):
#     payment_id=models.CharField(max_length=100)
#     order_id=models.CharField(max_length=100,null=False)
#     user_product=models.ForeignKey(UserProduct,on_delete=CASCADE,null=True)
#     product=models.ForeignKey(Product,on_delete=CASCADE)
#     user=models.ForeignKey(User,null=False,on_delete=CASCADE)
#     date=models.DateTimeField(auto_now_add=True)
#     status=models.BooleanField(default=False)

#     def __str__(self):
#         return self.user

class Order(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    payment_type=models.CharField(max_length=200,default="")
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100,null=True,blank=True)
    # payment_Mode=models.CharField(max_length=100,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    # def save(self):
    #     account_sid = 'ACfe07ad62de81bed49dde1d651f2c294d'
    #     auth_token = '39291923e0fd69ad1d991a7bf898c807'
    #     client = Client(account_sid, auth_token)

    #     message = client.messages.create(
    #                  body=f"Congratulations!!! {self.name} has ordered   Total amount {self.amount}",
    #                  from_='+18305327027',
    #                  to='+919811005027'
    #              )

    #     print(message.sid)

    #     return super().save()


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=CASCADE)
    product=models.CharField(max_length=100)
    image=models.ImageField(upload_to='proimage')
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    total=models.CharField(max_length=100)

    def __str__(self):
        return self.product

    def save(self):
        account_sid = 'ACfe07ad62de81bed49dde1d651f2c294d'
        auth_token = '39291923e0fd69ad1d991a7bf898c807'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     body=f"Product has ordered names - {self.product} and Quantity is {self.quantity} and total amount is {self.total}",
                     from_='+18305327027',
                     to='+919811005027'
                 )

        # print(message.sid)

        return super().save()
