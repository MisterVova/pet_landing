from ..models.group import Group
from django.contrib import admin


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", ]
