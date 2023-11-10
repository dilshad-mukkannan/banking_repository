from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('form/',views.create_form,name='form')

]