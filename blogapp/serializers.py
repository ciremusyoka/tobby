from rest_framework import serializers
from .models import Blog
from imagesapp.serializers import ImageSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','category','title','top_description','image_one','image_two','image_three','bottom_description')

class BlogPreviewSerializer(serializers.ModelSerializer):
    image_one = ImageSerializer()
    image_two = ImageSerializer()
    image_three = ImageSerializer()
    description = serializers.SerializerMethodField()
    cat = serializers.SerializerMethodField()
    card_image = serializers.SerializerMethodField()
    image_1 = serializers.SerializerMethodField()
    image_2 = serializers.SerializerMethodField()
    image_3 = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields =('id','cat','title','category','top_description','image_one','image_two','image_three',
                 'bottom_description','description', 'card_image', 'image_1', 'image_2', 'image_3')
    def get_card_image(self,obj):
        return self.request.build_absolute_uri(obj.image_one.card_image.url)

    def get_image_1(self,obj):
        return self.request.build_absolute_uri(obj.image_one.details_image.url)

    def get_image_2(self, obj):
        return self.request.build_absolute_uri(obj.image_two.details_image.url)

    def get_image_3(self, obj):
        return self.request.build_absolute_uri(obj.image_three.details_image.url)

    def get_description(self,obj):
        if not obj.top_description:
            return None
        self.request = self.context.get("request")
        return ( obj.top_description[3:150])

    def get_cat(self,obj):
        return obj.get_category_display()
