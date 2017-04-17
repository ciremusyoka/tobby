from django.shortcuts import render
from .models import Personal
from .serializers import AboutSerializer,LandingPageSerializer
from rest_framework import generics

class LandingPageList(generics.ListAPIView):
    serializer_class = LandingPageSerializer
    queryset = Personal.objects.filter(landing_image=True).order_by('?')[:1]

class AboutList(generics.ListAPIView):
    serializer_class = AboutSerializer
    queryset = Personal.objects.filter(about_image=True).order_by('?')[:1]