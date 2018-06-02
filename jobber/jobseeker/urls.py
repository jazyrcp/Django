from django.conf.urls import url
from django.contrib import admin

from jobseeker.views import HomeView,SeekerCreateView,ApplyView,ReviewView,JobView,EmployerView,SearchView,ChangePwd

urlpatterns = [
    url(r'^home',HomeView.as_view(),name='home'),
    url(r'^usercreate',SeekerCreateView.as_view(),name='newuser'),
    url(r'^applyj/(?P<jid>\d+)/$',ApplyView.as_view(),name='applyj'),
    url(r'^review/(?P<fid>\d+)/$',ReviewView.as_view(),name='review'),
    url(r'^jobs/(?P<cid>\w+)/$',JobView.as_view(),name='jobs'),
    url(r'^employer/(?P<pk>\d+)/$',EmployerView.as_view(),name='employer'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'changepwd/$',ChangePwd.as_view(),name='changepwd'),
]