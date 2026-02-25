from django.contrib import admin
from django.urls import path
from serverapp import views

urlpatterns = [
    path('', views.gst_bill, name='gst_bill'),
]