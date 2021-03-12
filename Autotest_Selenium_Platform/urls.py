"""Autotest_Selenium_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from Admin import views
from Admin.views import *
from Product.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login', views.login, name='login'),
    url(r'^register/$', views.register),
    url(r'^home/$', views.home),
    url(r'^', views.login, name='login'),
    # Login
    url(r'^api/browser', Public.data),
    url(r'^api/projectSummary', Public.index),
    #url(r'^api/barChar', Public.bar_char),
    #url(r'^api/lineChar', Public.line_char),

    # project
    url('^api/project/create', Project.create),

    url('^admin/home', home)

]
