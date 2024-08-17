"""
URL configuration for IEAPROJECT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmwpage',v.bmwpage,name='bmw'),
    path('Mercedes',v.Mercedes_page,name='m_ben'),
    path('Lamborghini',v.Lamborghini_page,name='ghine'),
    path('Porsche',v.Porsche_page,name='porsche'),
    path('Service',v.Service_page,name='service'),
    path('inc_search',v.inc_search,name='search'),
    path('filter',v.filter_by_date,name='filter'),
    path('details',v.service_details,name='details'),
    path('Ser_delete/<int:pk>',v.Ser_delete.as_view()),
    path('contact',v.contact_page,name='contact'),
    path('book',v.book_cars,name='book'),
    path('All_cars',v.all_cars,name='all'),
    path('Sports_cars',v.Sports_cars,name='sports'),
    path('comfort_cars',v.comfort_cars,name='comfort'),
    path('luxury_cars',v.luxury_cars,name='luxury'),
    path('bookcars',v.bookform,name='bookcar'),
    
    
        
]
