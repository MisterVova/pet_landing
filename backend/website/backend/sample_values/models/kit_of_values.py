from django.db import models
from sample_values.models.key_value import KeyValue


class KitOfValues(KeyValue):
    value = models.ManyToManyField(verbose_name='values', to=KeyValue, related_name='kit_of_values',)
    # tree = models.TextField(verbose_name="JSON", null=True)


    def get_value(self):
        # return self.__str__()
        arr = [item.get_value() for item in self.value.all()]
        ret = {self.kay: arr}
        return ret


    class Meta:
        ordering = ('name',)
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'
