from django.contrib import admin
from django.urls import path, include
from home import views
app_name='index'

urlpatterns = [
    path('', views.main),
]
