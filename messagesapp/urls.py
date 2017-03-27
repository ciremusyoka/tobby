from django.conf.urls import url
from .views import MessagesList

urlpatterns = [
    url(r'^messages$', MessagesList.as_view(), name='message'),

]