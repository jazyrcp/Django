from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from employer.views import EmpCreateView,EmpZoneView,NewJobView,login,ApplicationView,ReviewView,DeleteJob,ProfileView,EditJob,SendMailView,ForgotPwdView

urlpatterns = [
    url(r'^empcreate',EmpCreateView.as_view(),name='empcreate'),
    url(r'^ezone',EmpZoneView.as_view(),name='ezone'),
    url(r'^login',login,name='elogin'),
    url(r'^logout',auth_views.logout,{'template_name':'logout.html'},name='elogout'),
    url(r'^newjob',NewJobView.as_view(),name='newjob'),
    url(r'^appls',ApplicationView.as_view(),name='appls'),
    url(r'^viewrev',ReviewView.as_view(),name='viewrev'),
    url(r'^djob/(?P<jid>\d+)/$',DeleteJob.as_view(),name='djob'),
    url(r'^ejob/(?P<jid>\d+)/$',EditJob.as_view(),name='ejob'),
    url(r'^profile/(?P<sid>\d+)/$',ProfileView.as_view(),name='profile'),
    url(r'^sendmail/$',SendMailView.as_view(),name='sendmail'),
    url(r'^forgot/$',ForgotPwdView.as_view(),name='forgot'),
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)