from django.db import models

from sample_values.models.group import Group


class BaseValue(models.Model):
    name = models.CharField(verbose_name="Заголовок", max_length=64, unique=True, db_index=True)
    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE, related_name='values', null=True)

    def __str__(self):
        return f"{self.name}"

    def get_value(self):
        return "None"

    class Meta:
        ordering = ('-pk', 'name',)
        verbose_name = 'Свободные значение'
        verbose_name_plural = 'Свободные значения'
