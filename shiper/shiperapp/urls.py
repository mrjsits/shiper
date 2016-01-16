from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^order/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
	url(r'^order/$', views.order_new, name='order_new'),
]