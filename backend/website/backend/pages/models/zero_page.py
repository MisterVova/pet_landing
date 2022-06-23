from django.db import models
from garpix_page.models import BasePage


class ZeroPage(BasePage):
    template = "pages/zero.html"

    class Meta:
        verbose_name = "Zero"
        verbose_name_plural = "Zeros"
        ordering = ("-created_at",)
