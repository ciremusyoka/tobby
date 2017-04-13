from django.contrib import admin
from .models import Personal

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id','landing_image','about_image','image']

admin.site.register(Personal,PersonalAdmin)
