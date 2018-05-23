from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from shopname.views import HomeView,UserView,CategoryView,SubCategoryView,NewProductView
urlpatterns = [
   url(r'^home',HomeView.as_view(),name='home'),
   url(r'^new_user',UserView.as_view(),name = 'new_user'),
   url(r'^category/(?P<catname>\w+)/(?P<subname>\w+)/$',SubCategoryView.as_view(),name='subcat'),
   url(r'^category',CategoryView.as_view(),name='category'),
   url(r'^newproduct/$',NewProductView.as_view(),name='newproduct'),
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)