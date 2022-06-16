from ..models.image_value import ImageValue
from django.contrib import admin


@admin.register(ImageValue)
class ImageValueAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "pk"]
