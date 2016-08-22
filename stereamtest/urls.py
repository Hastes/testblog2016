"""stereamtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.front,name='posts'),
    url(r'^likepost/(\d+)/$',views.likepost,name='likepost'),
    url(r'^page/([0-9]+)/$', views.front, name='current_page'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article,name='article'),
    url(r'^article/(?P<article_id>\d+)/delete/$',views.delete_article,name='delete_article'),
    url(r'^article/(?P<article_id>\d+)/update/$',views.update_article,name='update_article'),
    url(r'^test/$',views.testpage),
    url(r'^test2/$',views.testpage2),
    url(r'^register/$', views.register_user,name='reg'),
    url(r'^login/$',views.login_user,name='login'),
    url(r'^logout/$',views.logout_user,name='logout'),
    url(r'^offtop/$',views.offtop, name='offtop'),
    url(r'^offtop/add/$',views.offtopjs),
    url(r'^offtop/reload/$',views.offtop_reload),
    url(r'^created/post/$',views.created_post,name='created_post'),
    url(r'^messagelike/(\d+)/$', views.message_like,name="message_like"),
    url(r'^deleteallmessage/$',views.delete_message,name="del_mes"),
    url(r'^blog/',include("blog.API.urls",namespace='blog_API')),
    url(r'^get_ip/$',views.get_ip_user,name='get_ip_user'),
]

from . import settings
import os
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
