from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from appfour.views import HomeView,BrandView,CarView,BigView,UserView,DeleteUser,DeleteUserS,EditUser,EditUserS,UserListView,login
urlpatterns = [
    url(r'^login/$',login,name='login'),
    url(r'^home/',HomeView.as_view(),name='home'),
    url(r'^logout/$',auth_views.logout,{'template_name' : 'logout.html'},name='logout'),
    url(r'^brand/',BrandView.as_view(),name='brand'),
    url(r'^car/',CarView.as_view(),name='car'),
    url(r'^big/',BigView.as_view(),name='big'),
    url(r'^user/',UserView.as_view(),name='user'),
    url(r'^delete/',DeleteUser.as_view(),name='delete'),
    url(r'^edit/',EditUser.as_view(),name='edit'),
    url(r'^userlist/',UserListView.as_view(),name='userlist'),
    url(r'^editl/([0-9]+)/$',EditUserS.as_view(),name='editl'),
    url(r'^deletel/([0-9]+)/$',DeleteUserS.as_view(),name='deletel'),

]
