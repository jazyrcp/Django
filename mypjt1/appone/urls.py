from django.conf.urls import url,include
from django.contrib import admin
from views import HomeView,StudentView,StudentListView
urlpatterns = [
    url(r'^home/',HomeView.as_view(),name='home'),
    url(r'^student/',StudentView.as_view(),name='student'),
    url(r'^stud_list/',StudentListView.as_view(),name='stud_list'),
   
]
