from django.db import models
from garpix_page.models import BasePage
from kit_of_values.models import Kit
from show.models import Template


class CasePage(BasePage):
    # template = "pages/case.html"
    template = "pages/zero.html"
    html_template = models.ForeignKey(verbose_name="html_template", to=Template, related_name="case_pages_html", on_delete=models.PROTECT)
    kit_template = models.ForeignKey(verbose_name="Набор Шаблонов", to=Kit, related_name="case_page_templates", on_delete=models.PROTECT)
    kit_values = models.ForeignKey(verbose_name="Набор Значений", to=Kit, related_name="case_page_values", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Case"
        verbose_name_plural = "Cases"
        ordering = ("-created_at",)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # print("self.kit_template.get_value()",self.kit_template.get_value())

        add_context = {
            "kit_of_templates": self.kit_template.get_value(),
            "kit_of_values": self.kit_values.get_value(),

        }

        context.update(add_context)
        return context
