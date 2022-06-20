from django.db import models
from garpix_utils.file import get_file_path

from kit_of_values.util import Node


class Group(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=64, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Value(models.Model):
    TYPE = "Base"
    name = models.CharField(verbose_name="Заголовок", max_length=64, db_index=True)
    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE, related_name='values')
    key = models.CharField(verbose_name="key", max_length=64, db_index=True, null=True, blank=True)
    type = models.CharField(verbose_name="Тип", max_length=16, db_index=True, null=False, blank=True, )

    def __str__(self):
        return f"{self.group} | {self.name} | {self.type} | {self.key}"

    def save(self, *args, **kwargs):
        self.type = self.TYPE
        super().save(*args, **kwargs)

    def get_value(self):
        return None

    class Meta:
        ordering = ('-pk', 'name',)
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class ImageValue(Value):
    TYPE = "Image"
    value = models.ImageField(verbose_name="Изображение", blank=False, null=False, upload_to=get_file_path, )

    def get_value(self):
        return self.value.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class FileValue(Value):
    TYPE = "File"
    value = models.FileField(verbose_name="Файл", blank=False, null=False, upload_to=get_file_path, )

    def get_value(self):
        return self.value.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class TextValue(Value):
    TYPE = "Text"
    value = models.TextField(verbose_name="Текст", null=True)

    def get_value(self):
        return self.value

    class Meta:
        ordering = ('name',)
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class SlugValue(Value):
    TYPE = "Slug"
    value = models.SlugField(max_length=150, verbose_name='ЧПУ', blank=False)

    def get_value(self):
        return self.value

    class Meta:
        ordering = ('name',)
        verbose_name = 'Slug'
        verbose_name_plural = 'Slugs'

class Kit(models.Model):
    name = models.CharField(verbose_name="Заголовок", max_length=64, db_index=True)
    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE, related_name='kits')
    values = models.ManyToManyField(verbose_name='values', to=Value, related_name='kits', blank=True)
    slug = models.SlugField(max_length=150, verbose_name='ЧПУ', unique=True, blank=False, db_index=True)

    def __str__(self):
        return f"{self.group} | {self.name}"

    def get_value(self):
        node = Node("kit_dict", None)
        for item in self.values.all():

            v = None
            if item.type == TextValue.TYPE:
                v = TextValue.objects.get(pk=item.pk)
            if item.type == ImageValue.TYPE:
                v = ImageValue.objects.get(pk=item.pk)
            if item.type == FileValue.TYPE:
                v = FileValue.objects.get(pk=item.pk)
            if item.type == SlugValue.TYPE:
                v = SlugValue.objects.get(pk=item.pk)

            if v:
                v = v.get_value()
            node.add_value(lst_key=self.split_key(item.key), value=v)
        return node.get_dict()

    def split_key(self, key):
        lst_k = f"{key}".strip().split(sep=".")
        lst_k = [f"{k}".strip() for k in lst_k]
        return lst_k

    class Meta:
        ordering = ('name',)
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'
