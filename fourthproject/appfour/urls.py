from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from appfour.views import HomeView,BrandView,CarView,BigView
urlpatterns = [
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^home/',HomeView.as_view(),name='home'),
    url(r'^logout/$',auth_views.logout,{'template_name' : 'logout.html'},name='logout'),
    url(r'^brand/',BrandView.as_view(),name='brand'),
    url(r'^car/',CarView.as_view(),name='car'),
    url(r'^big/',BigView.as_view(),name='big'),

]
