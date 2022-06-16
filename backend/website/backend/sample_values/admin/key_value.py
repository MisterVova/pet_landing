from django.contrib import admin
from ..models.key_value import KeyValue


@admin.register(KeyValue)
class KeyValueAdmin(admin.ModelAdmin):
    list_display = ["pk", "name",  "kay", ]
    list_display_links = ["pk", ]
    list_editable = ["name",  "kay", ]
    # list_select_related = ["basevalue_ptr", "keyandvalue", "keyandmanyvalue", "kitofvalues", ]
    # list_select_related = ["kitofvalues", ]
