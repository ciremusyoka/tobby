from django.shortcuts import render
from .models import Personal
from .serializers import AboutSerializer,LandingPageSerializer
from rest_framework import generics
from rest_framework import request
from django.http import HttpResponse
from imagekit import ImageSpec

class LandingPageList(generics.ListAPIView):
    serializer_class = LandingPageSerializer
    queryset = Personal.objects.filter(landing_image=True).order_by('?')[:1]

    # def get_queryset(self):
    #     queryset = Personal.objects.filter(landing_image=True).order_by('?')[:1]
    #     print (Personal.id)
    #     # queryset = Personal.objects.filter(landing_image=True).order_by('?')[:1]
    #     return HttpResponse(queryset, content_type="image/jpeg")
    # def landing_img(request):
    #     img = Personal.new()
    #     response = HttpResponse(extract(url), content_type="image/jpeg")
    #     img.save(response, "JPEG")
    #     return response

    # def my_image(request):
    #     image_data = open("/path/to/my/image.png", "rb").read()
    #     return HttpResponse(image_data, mimetype="image/png")

class AboutList(generics.ListAPIView):
    serializer_class = AboutSerializer
    queryset = Personal.objects.filter(about_image=True).order_by('?')[:1]