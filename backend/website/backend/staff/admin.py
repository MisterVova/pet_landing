from django.contrib import admin

from staff.models import Staff


@admin.register(Staff)
class ValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ["pk", "name", ]  # "__str__",
    list_editable = ["name",  ]
