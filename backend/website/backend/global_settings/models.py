from django.db import models
from solo.models import SingletonModel
from kit_of_values.models import Kit


class DemoGlobal(SingletonModel):
    kit_of_values = models.ForeignKey(verbose_name="Набор Значений", to=Kit, related_name="demo_global_values", on_delete=models.PROTECT)

    def __str__(self):
        return f'DemoGlobal {self.pk}'

    class Meta:
        verbose_name = "DemoGlobal"
        verbose_name_plural = "DemoGlobal"

