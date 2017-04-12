from django.shortcuts import render
from .pagination import Pages
from rest_framework import generics
from .serializers import BlogPreviewSerializer, BlogDetailsSerializer
from .models import Blog

class BlogList(generics.ListAPIView):
    serializer_class = BlogPreviewSerializer
    queryset = Blog.objects.all()
    pagination_class = Pages

    def filter_queryset(self, queryset):
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        if title is not None:
            queryset = queryset.filter (title__contains = title)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset.order_by('-id')

class BlogDetailList(generics.RetrieveAPIView):
    serializer_class = BlogDetailsSerializer
    queryset = Blog.objects.all()
