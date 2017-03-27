from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer, BlogPreviewSerializer
from .models import Blog

class BlogList(generics.ListAPIView):
    serializer_class = BlogPreviewSerializer
    queryset = Blog.objects.all()

    def filter_queryset(self, queryset):
        title = self.request.query_params.get('title', None)
        category = self.request.query_params.get('category', None)
        if title is not None:
            queryset = queryset.filter (title__contains = title)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset