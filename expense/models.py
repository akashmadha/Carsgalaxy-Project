from django.db import models
from django.contrib.auth.models import User

class chousejender(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Miss', 'Miss'),
        ('Other', 'Other'),
    ]

    Chouse_jender = models.CharField(max_length=10, choices=TITLE_CHOICES)

    class Meta:
        db_table = 'chousejender'

    def __str__(self):
        return self.Chouse_jender


class ModelsChouse(models.Model):
    Model_names = models.CharField(max_length=100)

    class Meta:
        db_table = 'models_chouse'
    
    def __str__(self):
        return self.Model_names


class ChouseCentre(models.Model):
    Chouse_Centre = models.CharField(max_length=100)

    class Meta:
        db_table = 'chouse_centre'
    
    def __str__(self):
        return self.Chouse_Centre


class TestDrive(models.Model):
    Customer_name = models.CharField(max_length=100)
    Customer_fullname = models.CharField(max_length=50)
    Chouse_jender = models.ForeignKey(chousejender, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=True)
    Contact = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Models_chouse = models.ForeignKey(ModelsChouse, on_delete=models.CASCADE)
    Description = models.TextField(max_length=1000)
    Address = models.CharField(max_length=100, default='Address')
    Model_centers = models.ForeignKey(ChouseCentre, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")

    class Meta:
        db_table = 'test_drive'
        

# class cart(models.Model):
#      user = models.ForeignKey(User, on_delete=models.CASCADE)
#      product = models.ForeignKey(TestDrive,on_delete=models.CASCADE)

    #  class Meta:
    #     db_table = 'cart'

from django import forms

class ServiceForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = '__all__'




   