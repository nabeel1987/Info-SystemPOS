from django.db import models
#• Run python manage.py makemigrations to create migrations for those changes • Run python manage.py migrate to apply those changes to the database
# Create your models here.

class Other(models.Model):
    Name=models.CharField(max_length=200,default="")
    Quantity=models.IntegerField()
    SellPrice=models.IntegerField(null=True)
    Cost=models.IntegerField()

    choices_status={
        ('Available', 'Item is in Stock'),
        ('Sold', 'Item is out of Stock'),
        ('Dispatch','Item is on a way')
    }
    choices_type={
        ('New','New'),
        ('Old','Old'),
        ('Refurbished','Refurbished')
    }
    Brand=models.CharField(max_length=200,default="")
    Status=models.CharField(max_length=10,choices=choices_status,default="")
    Type=models.CharField(max_length=100,choices=choices_type,default="")
    def __str__(self):
        return self.Name

class Book(models.Model):
    Name=models.CharField(max_length=200)
    Quantity=models.IntegerField()
    SellPrice=models.IntegerField(null=True)
    Cost=models.IntegerField()
    Author=models.CharField(max_length=200)
    choices_status={
        ('Available', 'Item is in Stock'),
        ('Sold', 'Item is out of Stock'),
        ('Dispatch','Item is on a way')
    }
    choices_type={
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction')
    }
    Status=models.CharField(max_length=10,choices=choices_status,default="")
    Type=models.CharField(max_length=100,choices=choices_type,default="")

    def __str__(self):
        return self.Name
class Device(models.Model):
    Name=models.CharField(max_length=200)
    Quantity=models.IntegerField()
    SellPrice=models.IntegerField(null=True)
    Cost=models.IntegerField()
    Color=models.CharField(max_length=200,default="")


    choices_status={
        ('Available', 'Item is in Stock'),
        ('Sold', 'Item is out of Stock'),
        ('Dispatch','Item is on a way')
    }
    choices_type={
        ('New','New'),
        ('Old','Old'),
        ('Refurbished','Refurbished')
    }
    Brand=models.CharField(max_length=200,default="")
    Status=models.CharField(max_length=10,choices=choices_status,default="")
    Type=models.CharField(max_length=100,choices=choices_type,default="")

    class Meta: #This is to avoid to make another table of Device. THis device class will be used as parent class by other classes
        abstract=True

    def __str__(self):
        return self.Name   #>>> Laptop.objects.all()  <QuerySet [<Laptop: Lenovo Y700>]>

class Laptop(Device):
    pass

class Mobile(Device):
    pass
