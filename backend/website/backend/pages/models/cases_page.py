from django.db import models
from garpix_page.models import BaseListPage


class CasesPage(BaseListPage):
    paginate_by = 25
    template = 'pages/cases.html'

    class Meta:
        verbose_name = "Cases"
        verbose_name_plural = "Casess"
        ordering = ('-created_at',)
