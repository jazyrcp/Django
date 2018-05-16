from django.conf.urls import url,include
from django.contrib import admin
from views import HomeView,SampleView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home',HomeView.as_view(),name='home'),
    url(r'^sample/create',SampleView.as_view(),name='sample'),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$',auth_views.logout,{'template_name':'logout.html'},name='logout'),
    
]
