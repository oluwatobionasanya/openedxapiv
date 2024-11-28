"""
URLs for openedxapiv.
"""
from django.urls import path
from  openedxapiv.simple_list import SimpleGetAPI

urlpatterns = [
    path('api/v1/simple-get-data2', SimpleGetAPI.as_view(), name='simple-get-data2')
]