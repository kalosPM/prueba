#encoding:utf-8
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.login, name = 'home'),
]