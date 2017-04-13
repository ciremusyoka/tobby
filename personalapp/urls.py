from django.conf.urls import url
from .views import AboutList,LandingPageList

urlpatterns = [
    url(r'^about_image', AboutList.as_view(), name='about'),
    url(r'^landing_image', LandingPageList.as_view(), name='landing')
]