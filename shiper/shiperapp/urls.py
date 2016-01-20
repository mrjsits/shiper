from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
	url(r'introduce',views.introduce, name='introduce'),
	url(r'^$', views.loginview, name = 'loginview'),
	url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
	url(r'^order/$', views.order_new, name='order_new'),
	url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
	url(r'^ordershow/$', views.order_show, name='order_show'),
	url(r'^register/$',views.registerview, name ='registerview'),
	url(r'^login/$', views.loginview, name = 'loginview'),
	url(r'^logout/$', views.logoutview, name='logoutview')
]
