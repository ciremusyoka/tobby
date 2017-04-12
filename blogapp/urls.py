from django.conf.urls import url
from .views import BlogList, BlogDetailList

urlpatterns = [
    url(r'^blog$', BlogList.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)$', BlogDetailList.as_view(), name='blogid'),


]