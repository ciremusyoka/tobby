from django.conf.urls import url
from .views import ImageList

urlpatterns = [
    url(r'^images$', ImageList.as_view(), name='image'),
]