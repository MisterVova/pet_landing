from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
