"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include, re_path
from patapp import views
from patapp.views import image
from patapp.views import login
from patapp.views import dbtest
from patapp.views import setinfo
import xadmin
from patapp.views import timetest
from patapp.views import reply

urlpatterns = [
    re_path('xadmin/', xadmin.site.urls),
    path('admin/', admin.site.urls),
    path('image/', include('patapp.urls')),
    path('multimage/', image.getMultImage),
    path('login/', login.login),
    path('downloadImage/', dbtest.downloadImage),
    path('setinfo/', setinfo.setinfo),
    path('initinfopage/', timetest.initinfopage),
    path('reply/', reply.reply),

]
