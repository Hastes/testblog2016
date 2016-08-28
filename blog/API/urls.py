from django.conf.urls import url
from django.contrib import admin

from .views import Offtop_CommentAPIView,UserProfAPIView


urlpatterns=[
    url(r'^api/$',Offtop_CommentAPIView.as_view(),name='api'),
    url(r'^api/user_prof/$',UserProfAPIView.as_view(),name='api')
]
