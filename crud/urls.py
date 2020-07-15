from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    #path('',views.home,name='home')
    path('',views.index,name='index'),
]