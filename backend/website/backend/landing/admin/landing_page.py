from ..models.landing_page import LandingPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(LandingPage)
class LandingPageAdmin(BasePageAdmin):
    pass
