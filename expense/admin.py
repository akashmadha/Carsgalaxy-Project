from django.contrib import admin
from .models import chousejender, ModelsChouse, ChouseCentre, TestDrive

# Registering the models with the admin site
admin.site.register(chousejender)
admin.site.register(ModelsChouse)
admin.site.register(ChouseCentre)
admin.site.register(TestDrive)

