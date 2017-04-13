from rest_framework import serializers
from .models import Personal

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ('__all__')

class LandingPageSerializer(serializers.ModelSerializer):
    landing_img = serializers.SerializerMethodField()
    class Meta:
        model = Personal
        fields = ('id', 'landing_img', 'landing_image')

    def get_landing_img(self,obj):
        if not obj.image:
            return not None
        self.request = self.context.get('request')
        return self.request.build_absolute_uri(obj.image.url)

class AboutSerializer(serializers.ModelSerializer):
    about_img = serializers.SerializerMethodField()
    class Meta:
        model = Personal
        fields = ('id','about_image', 'about_img')

    def get_about_img(self,obj):
        if not obj.image:
            return None
        self.request = self.context.get('request')
        return self.request.build_absolute_uri(obj.about_img.url)