__author__ = 'Rom54'

from django.conf.urls import url
from trash import views


urlpatterns=[
    url(r'^$',views.trashList),
]
