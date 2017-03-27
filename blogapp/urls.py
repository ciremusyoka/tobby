from django.conf.urls import url
from .views import BlogList

urlpatterns = [
    url(r'^blog', BlogList.as_view(), name='blog')
]