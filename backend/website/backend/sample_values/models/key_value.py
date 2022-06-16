from django.db import models
from sample_values.models import BaseValue


class KeyValue(BaseValue):
    kay = models.CharField(verbose_name="key", max_length=64, db_index=True)

    def __str__(self):
        return f"{self.kay} | {self.name}"

    def get_value(self):
        # v = None
        # if isinstance() : v =

        from sample_values.models import KitOfValues, KeyAndValue, KeyAndManyValue
        print(type(self))
        print("KeyValue", isinstance(self, KeyValue))
        print("KitOfValues", isinstance(self, KitOfValues))
        print("KeyAndValue", isinstance(self, KeyAndValue))
        print("KeyAndManyValue", isinstance(self, KeyAndManyValue))
        print("------------------")

        try:
            self.__class__= KeyAndManyValue
            print("KeyAndManyValue", isinstance(self, KeyAndManyValue))
            print(self.get_value())
        except: print("KeyAndManyValue err")

        ret = {self.kay: None}
        return ret

    class Meta:
        ordering = ('kay', '-pk', 'name',)
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'
