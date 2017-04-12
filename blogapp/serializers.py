from rest_framework import serializers
from .models import Blog
from rest_framework.pagination import PageNumberPagination

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','category','title','top_description','image_one','image_two','image_three','bottom_description')


class BlogPreviewSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    card_image = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields =('id','title','description','card_image', 'category')
    def get_card_image(self,obj):
        return self.request.build_absolute_uri(obj.image_one.card_image.url)


    def get_description(self,obj):
        if not obj.top_description:
            return None
        self.request = self.context.get("request")
        return ( obj.top_description[3:150])

class SimilarPreviewSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    cat = serializers.SerializerMethodField()


    class Meta:
        model = Blog
        fields =('id','cat','title','description', 'category')


    def get_description(self,obj):
        if not obj.top_description:
            return None
        self.request = self.context.get("request")
        return ( obj.top_description[3:150])



    def get_cat(self,obj):
        return obj.get_category_display()


class BlogDetailsSerializer(serializers.ModelSerializer):
    image_one = serializers.SerializerMethodField()
    image_two = serializers.SerializerMethodField()
    image_three = serializers.SerializerMethodField()
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()
    similar = serializers.SerializerMethodField()

    class Meta:
        model = Blog

        fields = ('id','category', 'title', 'top_description', 'image_one', 'image_two', 'image_three',
                   'bottom_description', 'image_1', 'image_2', 'image_3','similar' )

    def get_image_one(self, obj):
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image_one.image.url)

    def get_image_two(self, obj):
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image_two.image.url)

    def get_image_three(self, obj):
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image_three.image.url)

    def get_image_1(self, obj):
        self.request = self.context.get("request")
        return self.request.build_absolute_uri(obj.image_one.card_image.url)

    def get_image_2(self, obj):
        return self.request.build_absolute_uri(obj.image_two.card_image.url)

    def get_image_3(self, obj):
        return self.request.build_absolute_uri(obj.image_three.card_image.url)

    def get_similar(self, obj):
        queryset = Blog.objects.filter(category=obj.category, ).exclude(id=obj.id)
        serializer = BlogPreviewSerializer(queryset, many=True, context={'request': self.request}).data
        return serializer[-6:]