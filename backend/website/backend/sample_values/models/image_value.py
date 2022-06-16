from django.db import models

from sample_values.models import BaseValue
from garpix_utils.file import get_file_path


class ImageValue(BaseValue):
    # name = models.CharField(verbose_name="Заголовок", max_length=64, unique=True, db_index=True)
    image = models.ImageField(verbose_name="Изображение", blank=False, null=False, upload_to=get_file_path, )

    def get_value(self):
        ret = self.image
        return ret

    class Meta:
        ordering = ('name',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
