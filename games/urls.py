__author__ = 'Rom54'

from django.conf.urls import url
from django.contrib import admin
from games import views


urlpatterns=[
    url(r'^2048/$',views.game2048,name='2048'),
    url(r'^2048/score/$',views.score,name='score'),
    url(r'^painters/$',views.painters,name='painters'),
    url(r'^save_canvas/$',views.save_canvas,name="canvas")
]
