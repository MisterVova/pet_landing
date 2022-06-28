from django.db import models
from garpix_page.models import BasePage
from kit_of_values.models import Kit
from show.models import Template
from global_settings import global_context

class ZeroPage(BasePage):
    # template = "pages/zero.html"
    template = "pages/ttt.html"
    html_template = models.ForeignKey(verbose_name="html_template", to=Template, related_name="zero_pages_html", on_delete=models.PROTECT, null=True, blank=True)
    kit_template = models.ForeignKey(verbose_name="Набор Шаблонов", to=Kit, related_name="zero_page_templates", on_delete=models.PROTECT, null=True, blank=True)
    kit_values = models.ForeignKey(verbose_name="Набор Значений", to=Kit, related_name="zero_page_values", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Zero"
        verbose_name_plural = "Zeros"
        ordering = ("-created_at",)

    # def get_context(self, request=None, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     # print("self.kit_template.get_value()",self.kit_template.get_value())
    #
    #     add_context = {
    #         "kit_of_templates": self.kit_template.get_value(),
    #         "kit_of_values": self.kit_values.get_value(),
    #     }
    #
    #     context.update(add_context)
    #     return context
    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # print("self.kit_template.get_value()",self.kit_template.get_value())

        add_context = {
            "kit_of_templates": self.kit_template.get_value(),
            "kit_of_values": self.kit_values.get_value(),
            "global": global_context.global_context(request, self),
        }

        context.update(add_context)
        return context
