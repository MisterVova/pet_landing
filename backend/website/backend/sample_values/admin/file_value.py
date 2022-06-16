from ..models.file_value import FileValue
from django.contrib import admin


@admin.register(FileValue)
class FileValueAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "pk"]

