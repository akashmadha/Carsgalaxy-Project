from django.contrib import admin
from .models import chousejender, ModelsChouse, ChouseCentre, TestDrive

class TestDriveAdmin(admin.ModelAdmin):
    list_display = ['Customer_name', 'Customer_fullname', 'Chouse_jender', 'Date', 'Contact','Email','Models_chouse','Description','Address','Model_centers']
    search_fields = ['Customer_name', 'Customer_fullname', 'Chouse_jender', 'Date']


# Registering the models with the admin site
admin.site.register(chousejender)
admin.site.register(ModelsChouse)
admin.site.register(ChouseCentre)
admin.site.register(TestDrive,TestDriveAdmin)

