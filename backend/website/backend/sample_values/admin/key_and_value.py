from django.contrib import admin
from ..models.key_and_value import KeyAndValue


@admin.register(KeyAndValue)
class KeyAndValueAdmin(admin.ModelAdmin):
    # list_display = ["name",  "kay", "pk"]
    list_display = ["pk", "name",  "kay", "value", ]
    list_display_links = ["pk", ]
    list_editable = ["name",  "kay", "value", ]