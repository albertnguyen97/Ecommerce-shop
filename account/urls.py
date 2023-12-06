from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('shop/', views.shop, name='shop'),
    path('register/', views.register, name='register'),
    path('settings/', views.setting, name='settings'),
    path('edit/', views.edit, name='edit')
]