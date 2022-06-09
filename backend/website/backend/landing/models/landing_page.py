from django.db import models
from garpix_page.models import BasePage


class LandingPage(BasePage):
    template = "pages/landing.html"

    class Meta:
        verbose_name = "Landing"
        verbose_name_plural = "Landings"
        ordering = ("-created_at",)
