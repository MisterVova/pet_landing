from ..models.cases_page import CasesPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(CasesPage)
class CasesPageAdmin(BasePageAdmin):
    pass
