from django.db import models

from sample_values.models import BaseValue
from garpix_utils.file import get_file_path


class FileValue(BaseValue):
    # name = models.CharField(verbose_name="Заголовок", max_length=64, unique=True, db_index=True)
    image = models.FileField(verbose_name="Файл", blank=False, null=False, upload_to=get_file_path,)

    def get_value(self):
        ret = self.image
        return ret

    class Meta:
        ordering = ('name',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
