from django.db import models

from sample_values.models import BaseValue


class TextValue(BaseValue):
    # name = models.CharField(verbose_name="Заголовок", max_length=64, unique=True, db_index=True)
    text = models.TextField(verbose_name="Текст", null=True)

    def get_value(self):
        ret = self.text
        return ret

    class Meta:
        ordering = ('name',)
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
