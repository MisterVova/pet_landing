from ..models.text_value import TextValue
from django.contrib import admin


@admin.register(TextValue)
class TextValueAdmin(admin.ModelAdmin):
    list_display = ["name", "text", "pk"]
