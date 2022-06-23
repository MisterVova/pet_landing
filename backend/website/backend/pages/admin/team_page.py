from ..models.team_page import TeamPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(TeamPage)
class TeamPageAdmin(BasePageAdmin):
    pass
