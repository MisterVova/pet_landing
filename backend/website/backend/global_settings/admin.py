from django.contrib import admin

from global_settings.models import DemoGlobal


@admin.register(DemoGlobal)
class DemoGlobalAdmin(admin.ModelAdmin):
    list_display = ["pk", "__str__", ]  # "__str__",
    # list_editable = ["kit_of_value", ]
