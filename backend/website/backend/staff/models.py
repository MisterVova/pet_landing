from django.db import models
from kit_of_values.models import Kit
# Create your models here.


class Staff(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64, unique=True, db_index=True)
    kit_values = models.ForeignKey(verbose_name="Набор ролей", to=Kit, related_name="staff_values", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name = 'Команда проекта'
        verbose_name_plural = 'Команды проектов'
