from django.contrib import admin
from django.urls import path, include
from .views import demo, new_page

urlpatterns = [
    path('', demo, name='demo'),
    path('new/', new_page, name='new_page' ),


]