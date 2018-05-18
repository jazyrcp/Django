from django.conf.urls import url,include
from django.contrib import admin

from footshop.views import ProductView,CategoryView,SubCatView


urlpatterns = [
    url(r'^product',ProductView.as_view(),name='product'),
    url(r'^cat',CategoryView.as_view(),name='cat'),
    url(r'^subcat',SubCatView.as_view(),name='subcat'),
]