from django.db import models
from garpix_page.models import BasePage


class TeamPage(BasePage):
    template = "pages/team.html"

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ("-created_at",)
