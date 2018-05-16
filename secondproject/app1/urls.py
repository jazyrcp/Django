from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from app1.views import FirstView,SecondView,SecondListView,FirstListView,ThirdView,HomeView

from django.contrib.auth import views as auth_views



urlpatterns = [
	url(r'^home',HomeView.as_view(),name='home'),

    url(r'^first',FirstView.as_view(),name='first'),
    url(r'^second',SecondView.as_view(),name='second'),
    url(r'^sec_list',SecondListView.as_view(),name='sec_list'),
    url(r'^fir_list',FirstListView.as_view(),name='fir_list'),
    url(r'^third',ThirdView.as_view(),name='third'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)