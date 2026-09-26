from django.db import models


# Create your models here.
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self): #tells Django what to display as the name of that object
        return self.name
   
    class Meta: # when providing it as category, in admin django will keep the name as categorys so to change that will use this line .
        verbose_name_plural = "categories"


   
class Product(models.Model):
    name= models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2 , max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # foreignkey - connect one table to another, if the category was deleted all the related items will be deleted
    description=models.CharField(max_length=250, default='', blank=True , null=True) # if we don't need to type a description, we dont have to.
    image=models.ImageField(upload_to='uploads/product/')
    #add sale stuff
    is_sale = models.BooleanField(default=False) #not on sale
    sale_price = models.DecimalField(default=0, decimal_places=2 , max_digits=6)
    def __str__(self):
        return self.name
   


