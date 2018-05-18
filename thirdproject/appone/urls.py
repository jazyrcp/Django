from django.conf.urls import url,include
from django.contrib import admin
from appone.views import StudentView,StudentListView,TeacherView,TeacherListView,HomeView,HodView,HodListView,PrinceView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # url(r'^student/create',views.studview,name='student'),
    url(r'^home',HomeView.as_view(),name='home'),
    url(r'^student/create',StudentView.as_view(),name='student'),
    url(r'^list',StudentListView.as_view(),name='stud_list'),
    url(r'^teacher',TeacherView.as_view(),name='teacher'),
    url(r'^tlist',TeacherListView.as_view(),name='teacher_list'),
    url(r'^hod_list',HodListView.as_view(),name='hod_list'),
    url(r'^hod',HodView.as_view(),name='hod'),
    url(r'^prince',PrinceView.as_view(),name='prince'),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name="login"),
    url(r'^logout/$',auth_views.logout,{'template_name':'logout.html'},name="logout"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]