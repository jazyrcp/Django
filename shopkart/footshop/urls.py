from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login
from footshop.views import ProductView,CategoryView,SubCatView,HomeView,CustomerView,ProductListView,ProductDetailView,AddCartView


urlpatterns = [
url(r'^login/$',login,{'template_name':'login.html'},name='login'),
    url(r'^product',ProductView.as_view(),name='product'),
    url(r'^cat',CategoryView.as_view(),name='cat'),
    url(r'^subcat',SubCatView.as_view(),name='subcat'),
    url(r'^home',HomeView.as_view(),name='home'),
    url(r'^cust',CustomerView.as_view(),name='cust'),
    url(r'^prolist',ProductListView.as_view(),name='prolist'),
    url(r'^detail/(?P<pk>[0-9]+)/$',ProductDetailView.as_view(),name='prodetail'),
    url(r'^addcart',AddCartView.as_view(),name='addcart'),
]
