from django.db import models
from garpix_page.models import BasePage


class CasePage(BasePage):
    template = "pages/case.html"

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"
        ordering = ("-created_at",)
