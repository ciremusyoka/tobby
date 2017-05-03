from django.shortcuts import render
from .models import Image
from .serializers import ImageSerializer,previewSerializers
from rest_framework import generics
from .pagination import Pages

class ImageList (generics.ListAPIView):
    serializer_class = previewSerializers
    queryset = Image.objects.all()
    pagination_class = Pages



    def get_queryset(self):
        return Image.objects.filter(public=True)
    def filter_queryset(self, queryset):
        category = self.request.query_params.get('category', None)
        featured = self.request.query_params.get('featured', None)
        if (category == ''):
            category = None
        if (featured == ''):
            featured = None
        if category is not None:
            queryset = queryset.filter(category  = category)
        if featured is not None:
            queryset = queryset.filter(featured = featured)
        return queryset.order_by('-id')
