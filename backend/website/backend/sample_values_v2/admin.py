from django.contrib import admin

from .models import Group, Value, TextValue, ImageValue, FileValue, Kit


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", ]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "group", "type", "key" , "__str__"]


@admin.register(TextValue)
class TextValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", ]
    list_editable = ["name", "key",  ]
    # list_editable = [ "key", ]


@admin.register(ImageValue)
class ImageValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", ]


@admin.register(FileValue)
class FileValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", ]


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ["name", "group", "__str__"]

