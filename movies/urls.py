__author__ = 'Rom54'

from django.conf.urls import url
from movies import views


urlpatterns=[
    url('^$',views.listMovies,name='listMovies'),
    url('^tag/(?P<slug>[-\w]+)/$',views.listForTags,name='urltags'),
    url('^like/(?P<inf>\w+)/(?P<id>\d+)/$',views.like,name='like'),
]
