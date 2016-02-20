# -*- coding: utf-8 -*-
from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^serach_list/$', views.serach_list, name='serach_list'),   # 一覧
]
