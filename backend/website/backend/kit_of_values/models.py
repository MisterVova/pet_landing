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
        return f"{self.name} | {self.group} | {self.type} | {self.key}"

    #
    # def get_str(self):
    #     return f"{self.group}|{self.type}|{self.key}"

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
        # ret = super().get_value()
        # ret["url_i"] = self.value.name
        # return ret
        return self.value.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class FileValue(Value):
    TYPE = "File"
    value = models.FileField(verbose_name="Файл", blank=False, null=False, upload_to=get_file_path, )

    def get_value(self):
        # ret = super().get_value()
        # ret["url_f"] = self.value.name
        # return ret
        return self.value.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class TextValue(Value):
    TYPE = "Text"
    value = models.TextField(verbose_name="Текст", null=True)

    def get_value(self):
        # ret = super().get_value()
        # ret["text"] = self.value
        # return ret
        return self.value

    class Meta:
        ordering = ('name',)
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Kit(models.Model):
    name = models.CharField(verbose_name="Заголовок", max_length=64, db_index=True)
    group = models.ForeignKey(verbose_name='Группа', to=Group, on_delete=models.CASCADE, related_name='kits')
    values = models.ManyToManyField(verbose_name='values', to=Value, related_name='kits', blank=True)
    slug = models.SlugField(max_length=150, verbose_name='ЧПУ', unique=True, blank=True, default='', db_index=True)

    def __str__(self):
        return f"{self.name} | {self.group}"

    def get_value(self):
        ret = dict()
        node = Node("kit_dict", None)
        for item in self.values.all():

            v = None
            if item.type == TextValue.TYPE:
                v = TextValue.objects.get(pk=item.pk)
            if item.type == ImageValue.TYPE:
                v = ImageValue.objects.get(pk=item.pk)
            if item.type == FileValue.TYPE:
                v = FileValue.objects.get(pk=item.pk)

            if v:
                v = v.get_value()

            # self.add_value_in_kit_dict(kit_dict=ret, lst_key=self.split_key(item.key), value=v)

            node.add_value(lst_key=self.split_key(item.key),value=v)

            # node.get_dict()
        # print(node)
        return node.get_dict()

    # def add_value_in_kit_dict(self, kit_dict: dict, lst_key: list, value):
    #
    #     def is_list_key(key):
    #         if "[" in key:
    #             return True
    #         return False
    #
    #     def add_value_in_dict(ret_dict: dict, lst_key: list, value):
    #         if len(lst_key) < 1:
    #             # key = "[]"
    #             # self.add_value_in_dict(kit_dict=kit_dict, lst_key=[key], value=value)
    #             return
    #
    #         if len(lst_key) == 1:
    #             key = lst_key[0]
    #             ret_dict[key] = value
    #             return
    #
    #         key = lst_key.pop(0)
    #         if not key in ret_dict.keys():
    #             if lst_key[0] == "[]":
    #                 ret_dict[key] = list()
    #             else:
    #                 ret_dict[key] = dict()
    #
    #         if type(ret_dict[key]) == list:
    #             add_value_in_list(ret_list=ret_dict[key], lst_key=lst_key, value=value)
    #         if type(ret_dict[key]) == dict:
    #             add_value_in_dict(ret_dict=ret_dict[key], lst_key=lst_key, value=value)
    #
    #     def add_value_in_list(ret_list: list, lst_key: list, value):
    #         key = lst_key.pop(0)
    #
    #         item = {"ord": "", "value": value, "key": key, "lst_key": lst_key}
    #         ret_list.append(item)
    #
    #     def add_value_in_obj(obj, key, value, lst_key: list):
    #         # if len(lst_key) < 1:
    #         #     # key = "[]"
    #         #     # self.add_value_in_dict(kit_dict=kit_dict, lst_key=[key], value=value)
    #         #     return
    #         #
    #         # if len(lst_key) == 1:
    #         #     key = lst_key[0]
    #         #     kit_dict[key] = value
    #         #     return
    #         #
    #         # if type(obj) == list:
    #         #     add_value_in_list(ret_list=kit_dict[key], lst_key=lst_key, value=value)
    #         # if type(obj) == dict:
    #         #     add_value_in_dict(ret_dict=obj, lst_key=lst_key, value=value)
    #         child = None
    #         if is_list_key(key):
    #             pass
    #         else:
    #             pass
    #
    #
    #     if len(lst_key) < 1:
    #         kit_dict["kit_dict"] = value
    #         return
    #
    #     key = lst_key.pop(0)
    #     add_value_in_obj(obj=kit_dict, key=key, value=value, lst_key=lst_key)

    def split_key(self, key):
        lst_k = f"{key}".strip().split(sep=".")
        #
        # ret = {}
        # for k in lst_k:
        #     ret
        lst_k = [ f"{k}".strip() for k in lst_k]
        # return ["kit_dict"] + lst_k
        return lst_k

    class Meta:
        ordering = ('name',)
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'


