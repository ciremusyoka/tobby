from django.shortcuts import render
from .models import Message
from .serializers import MessagesSerializer
from rest_framework import generics
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

class MessagesList(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        message=serializer.save()
        print (message.email)
        send_mail(message.name, message.message+" ( Phone: "+message.phone+ " Mail: "+message.email+ " )",
                  message.email, ['tobbylineclicks@gmail.com'])