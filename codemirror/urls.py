#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('codemirror.views',
    url(r'^savefile.html$', 'savefile'),
    url(r'^$', 'openfile'),
    
)
