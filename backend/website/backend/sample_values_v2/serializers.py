from rest_framework import serializers
from .models import Kit, TextValue, ImageValue, FileValue, Value


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = "__all__"
        # exclude = ("type",)


class TextValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextValue
        fields = "__all__"



class ImageValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageValue
        fields = "__all__"


class FileValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileValue
        fields = "__all__"



class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = "__all__"


class KitSerializer_v2(serializers.ModelSerializer):
    kit = serializers.SerializerMethodField()
    # values = TextValueSerializer(many=True)


    class Meta:
        model = Kit
        # fields = "__all__"
        fields = ["pk", "slug", "name", "kit", ]


    def get_kit(self, obj: Kit) -> dict:
        # ret = dict()
        # ret.update()
        # ret["abc"] = "123"
        # ret["kit_name"] = obj.name
        # ret["kit_tree"] = obj.get_value()
        # for item in obj.values.all():
        #     # item.dict_update(obj, ret)
        #
        #     # s = None
        #     # v = None
        #     # if item.type == TextValue.TYPE:
        #     #     # TextValue.dict_update(obj, ret)
        #     #     s = TextValueSerializer
        #     # if item.type == ImageValue.TYPE:
        #     #     s = ImageValueSerializer
        #     # if item.type == FileValue.TYPE:
        #     #     s = FileValueSerializer
        #     # if s:
        #     #     print(s)
        #     #     print(item)
        #     #     p = s(data=item)
        #     #     is_valid=p.is_valid()
        #     #     print(is_valid)
        #     #     print(p.validated_data)
        #     #     print(p.data)
        #     #     # v = p.validated_data
        #
        #     ret[item.key] = item.type
        return obj.get_value()
