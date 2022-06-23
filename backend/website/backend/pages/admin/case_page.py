from ..models.case_page import CasePage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(CasePage)
class CasePageAdmin(BasePageAdmin):
    pass
