
from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class SERVICE(models.Model):
    Customer_name=models.CharField(max_length=100)
    Customer_fullname=models.CharField(max_length=50)
    Date=models.DateField(auto_now=True)
    Contact=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Description=models.TextField(max_length=1000)
    Address=models.CharField(max_length=100,default='Address')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Model:
        db_table='service'

from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model=SERVICE
        fields='__all__'


class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    
    class Meta:
        db_table='category'

    def __str__(self):
        return self.category_name


#thise is bmw page        
class BmwModel(models.Model):
    img=models.ImageField(upload_to='image',default='')
    model_name=models.CharField(max_length=50)
    model_price=models.IntegerField()
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='bmwcar'

#thise is Mercedes-Benz page  
class MerModel(models.Model):
    img=models.ImageField(upload_to='image',default='')
    model_name=models.CharField(max_length=50)
    model_price=models.IntegerField()
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Mercar'

#thise is Lamborghene page
class lamModel(models.Model):
    img=models.ImageField(upload_to='image',default='')
    model_name=models.CharField(max_length=50)
    model_price=models.IntegerField()
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='lamcar'

#thise is Porsche page
class PorModel(models.Model):
    img=models.ImageField(upload_to='image',default='')
    model_name=models.CharField(max_length=50)
    model_price=models.IntegerField()
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='Porcar'




class BookCars(models.Model):
    Your_name = models.CharField(max_length=100)
    Your_fullname = models.CharField(max_length=50)
    Date = models.DateField(auto_now=True)
    Contact = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=100, default='Address')
    img=models.ImageField(upload_to='image',default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='booklist'