from .models import Template
from django.contrib import admin


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]  # "__str__",
    list_filter = ["destiny", ]
    list_editable = ["slug", ]
