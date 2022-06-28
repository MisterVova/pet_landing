from django.db import models
from garpix_page.models import BaseListPage

from global_settings import global_context
from kit_of_values.models import Kit
from show.models import Template


class CasesPage(BaseListPage):
    paginate_by = 25
    # template = 'pages/cases.html'
    template = "pages/zero.html"
    html_template = models.ForeignKey(verbose_name="html_template", to=Template, related_name="cases_pages_html", on_delete=models.PROTECT)
    kit_template = models.ForeignKey(verbose_name="Набор Шаблонов", to=Kit, related_name="cases_page_templates", on_delete=models.PROTECT)
    kit_values = models.ForeignKey(verbose_name="Набор Значений", to=Kit, related_name="cases_page_values", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Cases"
        verbose_name_plural = "Casess"
        ordering = ('-created_at',)

    def get_context(self, request=None, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # print("self.kit_template.get_value()",self.kit_template.get_value())
        paginated_object_list = context.get("paginated_object_list", [])
        kit_of_values = {}
        kit_of_values.update(self.kit_values.get_value())
        kit_of_values.update({"paginated_object_list": [{"title":item.title,"url":item.get_absolute_url(), "logo_url":item.logo.url} for item in paginated_object_list]})

        add_context = {
            "kit_of_templates": self.kit_template.get_value(),
            "kit_of_values": kit_of_values,
            "global": global_context.global_context(request, self),
        }

        context.update(add_context)
        return context
