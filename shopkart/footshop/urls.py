from django.conf.urls import url,include
from django.contrib import admin

from footshop.views import ProductView,CategoryView,SubCatView,HomeView,CustomerView


urlpatterns = [
    url(r'^product',ProductView.as_view(),name='product'),
    url(r'^cat',CategoryView.as_view(),name='cat'),
    url(r'^subcat',SubCatView.as_view(),name='subcat'),
    url(r'^home',HomeView.as_view(),name='home'),
    url(r'^cust',CustomerView.as_view(),name='cust'),
]
