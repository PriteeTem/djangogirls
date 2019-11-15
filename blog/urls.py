from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^about$', views.about_page, name='about_page'),
    url(r'^team$', views.team_page, name='team_page'),
    url(r'^events$', views.post_list, name='post_list'),
    url(r'^plaid_page$', views.plaid_page, name='plaid_page'),
    url(r'get_access_token$', views.get_access_token, name='get_access_token'),
]
