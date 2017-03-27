from django.shortcuts import render
from .models import Message
from .serializers import MessagesSerializer
from rest_framework import generics

class MessagesList(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer
    queryset = Message.objects.all()
