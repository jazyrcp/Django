from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth import views as auth_views

from shopname.views import HomeView,UserView,CategoryView,SubCategoryView,NewProductView,AddCartView,CartListView,DeleteCartView,CustomerView


urlpatterns = [
   url(r'^home/$',HomeView.as_view(),name='home'),
   url(r'^new_user/$',UserView.as_view(),name = 'new_user'),
   url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
   url(r'^logout/$',auth_views.logout,{'template_name':'home.html'},name='logout'),
   url(r'^category/$',CategoryView.as_view(),name='category'),
   url(r'^customer',CustomerView.as_view(),name='customer'),
   url(r'^newproduct/$',NewProductView.as_view(),name='newproduct'),
   url(r'^addcart/$',AddCartView.as_view(),name='addcart'),
   url(r'^deletecart/(?P<pid>\d+)/$',DeleteCartView.as_view(),name='deletecart'),
   url(r'^cart/(?P<uid>\w+)/$',CartListView.as_view(),name='cart'),
   url(r'^category/(?P<catname>\w+)/(?P<subname>\w+)/$',SubCategoryView.as_view(),name='subcat'),
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)