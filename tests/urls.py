# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


urlpatterns = [
    url(r'^', include('simple_notifications.urls')),
    url(r'', home, name="home"),
    url(r'test_one', home, name="test_url"),
]
