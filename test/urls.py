from django.contrib import admin
from django.urls import path
from .views import TestView


urlpatterns = [
    path('test/', TestView.as_view(), name='test_view'),
]
