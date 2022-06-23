from ..models.zero_page import ZeroPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(ZeroPage)
class ZeroPageAdmin(BasePageAdmin):
    pass
