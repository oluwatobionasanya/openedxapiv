"""
URLs for openedxapiv.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from simple_list import SimpleGetAPI

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="openedx_custom_api/base.html")),
    path('api/v1/simple-get-data2', SimpleGetAPI.as_view(), name='simple-get-data2')
]