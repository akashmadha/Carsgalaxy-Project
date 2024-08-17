"""
URL configuration for encome_expence_account project.

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
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home,name='home'),
    path('registration',v.add_user,name='reg'),
    path('login/',v.loginform,name='login'),
    path('logout/',v.logout_v,name='logout'),
    #  path('forgot_password/', v.forgot_password, name='forgot_password'),

    # path('password_reset/', 
    #      auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), 
    #      name='password_reset'),
    # path('password_reset/done/', 
    #  auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
    #  name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', 
    #      auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_email.html'), 
    #      name='password_reset_email'),
    # path('reset/done/', 
    #      auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
    #      name='password_reset_complete'),
]
