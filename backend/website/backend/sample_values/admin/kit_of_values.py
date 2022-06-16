from django.contrib import admin
from ..models.kit_of_values import KitOfValues


@admin.register(KitOfValues)
class KitOfValuesAdmin(admin.ModelAdmin):
    # list_display = ["name",  "kay", "pk"]
    list_display = ["pk", "name",  "kay", ]
    list_display_links = ["pk", ]
    list_editable = ["name",  "kay", ]
