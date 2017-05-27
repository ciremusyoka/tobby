from rest_framework import serializers
from .models import Blog
from rest_framework.pagination import PageNumberPagination

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','category','title','description','image' ,'preview')


class BlogPreviewSerializer(serializers.ModelSerializer):
    mypreview = serializers.SerializerMethodField()
    card_image = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields =('id','title','card_image', 'category', 'mypreview')
    def get_card_image(self,obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image.card_image.url)


    def get_mypreview(self,obj):
        if not obj.preview:
            return None
        self.request = self.context.get("request")
        return ( obj.preview[0:150])

class SimilarPreviewSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    cat = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields =('id','cat','title','preview', 'category')


    def get_description(self,obj):
        if not obj.preview:
            return None
        self.request = self.context.get("request")
        return ( obj.preview[3:150])



    def get_cat(self,obj):
        return obj.get_category_display()


class BlogDetailsSerializer(serializers.ModelSerializer):
    image_one = serializers.SerializerMethodField()
    similar = serializers.SerializerMethodField()

    class Meta:
        model = Blog

        fields = ('id','category', 'title', 'description', 'image_one', 'image', 'similar','preview' )

    def get_image_one(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image.image.url)

    # card images
    def get_image(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image.card_image.url)

    def get_similar(self, obj):
        queryset = Blog.objects.filter(category=obj.category, ).exclude(id=obj.id)
        serializer = BlogPreviewSerializer(queryset, many=True, context={'request': self.request}).data
        return serializer[-6:]