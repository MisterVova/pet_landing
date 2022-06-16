from ..models.base_value import BaseValue
from django.contrib import admin


@admin.register(BaseValue)
class BaseValueAdmin(admin.ModelAdmin):
    list_display = ["name", "pk", "keyvalue", ]

    # list_select_related = ["textvalue", "imagevalue", "filevalue", "keyvalue", ]
    list_select_related = [ "keyvalue", ]