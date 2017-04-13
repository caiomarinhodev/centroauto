"""default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from app.views.ClientView import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),
    url(r'^$', ClienteList.as_view(), name='list'),
    url(r'^create/$', ClienteCreate.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name='edit'),
    # url(r'^view/(?P<pk>\d+)/$', Cliente.as_view(), name='view'),
    url(r'^delete/(?P<pk>\d+)/$', ClienteDelete.as_view(), name='delete'),
]
