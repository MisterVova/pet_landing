from django.db import models
from sample_values.models import BaseValue
from sample_values.models.key_value import KeyValue


class KeyAndValue(KeyValue):
    value = models.ForeignKey(verbose_name='value', to=BaseValue, on_delete=models.CASCADE, related_name='key_and_value', null=False)

    # def __str__(self):
    #     return f"{self.kay}"

    def get_value(self):
        ret = {self.kay: self.value.get_value()}
        return ret

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пара Ключ Значение'
        verbose_name_plural = 'Пары Ключей и Значений'
