"""Django_sample URL Configuration

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
from django.contrib import admin
from django.conf.urls import url
# from django_web.views import index
from django_web.views import chart
from django_web.views import highchart
# from django_web.views import caselist
from django_web.views import map
from django_web.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/',index),
    url(r'^chart/',chart),
    url(r'^highchart/',highchart),
    # url(r'^caselist/',caselist),
    url(r'^map/',map),
    url(r'^pro_ershoufang/',pro_ershoufang),
    url(r'^user_jingji/',user_jingji),
    url(r'^login/',login),
    url(r'^reg/',reg),
    url(r'^user/',user),
    url(r'^user_guanzhu/',user_guanzhu),
    url(r'^user_pwd/',user_pwd),
    url(r'^user_shengqing/',user_shengqing),
    url(r'^about/',about),
    url(r'^proinfo/',proinfo),
    url(r'^admin_add/',admin_add),
    url(r'^mlogin/',mangerlogin),
    url(r'^admin_cate/',admin_cate),
    url(r'^admin_edit/',admin_edit),
    url(r'^admin_list/',admin_list),
    url(r'^admin_role/',admin_role),
    url(r'^admin_rule/',admin_rule),
    url(r'^member_add/',member_add),
    url(r'^member_del/',member_del),
    url(r'^member_edit/',member_edit),
    url(r'^member_list/',member_list),
    url(r'^member_pas/',member_pas),
    url(r'^index/',index),

]
