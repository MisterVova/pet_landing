from django.db import models
from sample_values.models import BaseValue
from sample_values.models.key_value import KeyValue


class KeyAndManyValue(KeyValue):
    values = models.ManyToManyField(verbose_name='values', to=BaseValue, related_name='key_and_many_values')

    def get_value(self):
        # return "ret KeyAndManyValue"
        # arr = self.values.objects.all().get_value()
        arr = [item.get_value() for item in self.values.all()]
        ret = {self.kay: arr}
        return ret

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пара Ключ и Списка Значении'
        verbose_name_plural = 'Пары Ключей и Списков Значений'
