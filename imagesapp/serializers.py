from rest_framework import serializers
from .models import Image
from colorthief import ColorThief
from django.conf import settings



class ImageSerializer (serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')


class previewSerializers (serializers.ModelSerializer):
    preview_xxs = serializers.SerializerMethodField()
    preview_xs = serializers.SerializerMethodField()
    preview_s = serializers.SerializerMethodField()
    preview_m  = serializers.SerializerMethodField()
    preview_l = serializers.SerializerMethodField()
    preview_xl = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    raw = serializers.SerializerMethodField()
    dominantColor = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields=('id','category','featured','name','preview_xxs','preview_xs','preview_s','preview_m','preview_l','preview_xl','raw','dominantColor')


    def rgb_to_hex(self,rgb):
        return '#' + '%02x%02x%02x' % rgb

    def get_dominantColor(self,obj):
        if not obj.dominantColor:
                # tenserflow
            ##Calculate and update db
            path = ColorThief(settings.MEDIA_ROOT+"/"+self.get_name(obj)).get_color()
            obj.dominantColor = self.rgb_to_hex(path)
            obj.save()
        #Else return the earlier calculated color
        return obj.dominantColor

    def get_preview_xxs(self,obj):
        if not obj.image:
            return None
        self.request=self.context.get("request")
        return {"width":obj.preview_xxs.width,"height":obj.preview_xxs.height, "path":self.request.build_absolute_uri(obj.preview_xxs.url)}

    def get_preview_xs(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return {"width": obj.preview_xs.width, "height": obj.preview_xs.height,
                "path": self.request.build_absolute_uri(obj.preview_xs.url) }

    def get_preview_s(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return {"width": obj.preview_s.width, "height": obj.preview_s.height,
                "path": self.request.build_absolute_uri(obj.preview_s.url)}

    def get_preview_m(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return {"width": obj.preview_m.width, "height": obj.preview_m.height,
                "path": self.request.build_absolute_uri(obj.preview_m.url)}

    def get_preview_l(self, obj):
        if not obj.image:
            return None
        self.request = self.context.get("request")
        return {"width": obj.preview_l.width, "height": obj.preview_l.height,
                "path": self.request.build_absolute_uri(obj.preview_l.url)}

    def get_preview_xl(self, obj):
        if not obj.image:
            return None
        self.request =self.context.get("request")
        return {"width":obj.preview_xl.width, "height":obj.preview_xl.height,
                "path":self.request.build_absolute_uri(obj.preview_xl.url)}

    def get_raw(self,obj):
        if not obj.image:
            return None
        self.request=self.context.get("request")
        return {"width":obj.image.width,"height":obj.image.height ,
                "path":self.request.build_absolute_uri(obj.image.url)}

    def get_name(self,obj):
        if not obj.image:
            return None
        self.request=self.context.get("request")
        return (obj.image.name)


