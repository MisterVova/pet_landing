from django.contrib import admin
from ..models.key_and_many_values import KeyAndManyValue


@admin.register(KeyAndManyValue)
class KeyAndManyValueAdmin(admin.ModelAdmin):
    list_display = ["name", "kay", "pk"]
