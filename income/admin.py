from django.contrib import admin
from .models import Category, MerModel, lamModel, PorModel, BmwModel,PayMent

# Define your admin classes with search fields
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description']
    search_fields = ['category_name', 'description']

class MerModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'description', 'category', 'img']
    search_fields = ['model_name', 'model_price', 'description', 'category__category_name']

class LamModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'description', 'category', 'img']
    search_fields = ['model_name', 'model_price', 'description', 'category__category_name']

class PorModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'description', 'category', 'img']
    search_fields = ['model_name', 'model_price', 'description', 'category__category_name']

class BmwModelAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_price', 'description', 'category', 'img']
    search_fields = ['model_name', 'model_price', 'description', 'category__category_name']


class PayMentAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'payment_id', 'paid']
    search_fields = ['Name']

# class BookCarsAdmin(admin.ModelAdmin):
#     list_display = ['Your_name', 'Your_fullname', 'Date', 'Contact', 'Email' , 'Address', 'user']
#     search_fields = ['Your_name', 'Your_fullname', 'Date', 'Contact', 'Email' , 'Address']

# Register your models and their admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(MerModel, MerModelAdmin)
admin.site.register(lamModel, LamModelAdmin)
admin.site.register(PorModel, PorModelAdmin)
admin.site.register(BmwModel, BmwModelAdmin)
admin.site.register(PayMent, PayMentAdmin)
# admin.site.register(BookCars, BookCarsAdmin)
