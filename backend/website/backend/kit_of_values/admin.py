from django.contrib import admin

from .models import Group, Value, TextValue, ImageValue, FileValue, Kit, SlugValue, CharValue


class SlugInline(admin.TabularInline):
    model = SlugValue


class CharInline(admin.TabularInline):
    model = CharValue


class TextInline(admin.TabularInline):
    model = TextValue


class ImageInline(admin.TabularInline):
    model = ImageValue


class FileInline(admin.TabularInline):
    model = FileValue


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    inlines = [SlugInline, CharInline, ImageInline, FileInline, TextInline, ]


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ["pk", "name", "group", "key", "type", ]  # "__str__",
    list_filter = ["group", "type", ]
    list_editable = ["name", "key", "group", ]


@admin.register(TextValue)
class TextValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", "type",]
    list_editable = ["name", "key", ]
    # list_editable = [ "key", ]


@admin.register(SlugValue)
class SlugValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", ]
    list_editable = ["name", "key", "group", "value"]


@admin.register(CharValue)
class CharValueAdmin(ValueAdmin):
    # pass
    list_display = ValueAdmin.list_display + ["value", ]
    list_editable = ["name", "key", "group", "value"]


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
