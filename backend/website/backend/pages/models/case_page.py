from django.db import models
from garpix_page.models import BasePage

from global_settings import global_context
from kit_of_values.models import Kit, Tag
from show.models import Template
from garpix_utils.file import get_file_path

from staff.models import Staff


class CasePage(BasePage):
    # template = "pages/case.html"
    # template = "pages/zero.html"
    template = "pages/ttt.html"
    description = models.TextField(verbose_name="Описание", default="")
    logo = models.FileField(verbose_name="Логотип", blank=True, upload_to=get_file_path, )
    banner = models.FileField(verbose_name="Баннер", blank=True, upload_to=get_file_path, )
    color_bg = models.CharField(verbose_name="Цвет Фона", max_length=9, blank=True)
    color_nuance = models.CharField(verbose_name="Цвет Нюанса", max_length=9, blank=True)
    color_text = models.CharField(verbose_name="Цвет Текста", max_length=9, blank=True, )
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="case_pages", blank=True)

    html_template = models.ForeignKey(verbose_name="html_template", to=Template, related_name="case_pages_html", on_delete=models.PROTECT)
    kit_template = models.ForeignKey(verbose_name="Набор Шаблонов", to=Kit, related_name="case_page_templates", on_delete=models.PROTECT)
    kit_values = models.ForeignKey(verbose_name="Набор Значений", to=Kit, related_name="case_page_values", on_delete=models.PROTECT)

    team = models.ForeignKey(verbose_name="Команда проекта", to=Staff, related_name="case_page_staffs", on_delete=models.PROTECT)

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
            "global": global_context.global_context(request, self),
        }

        context.update(add_context)
        return context
