from rest_framework import serializers
from ..models import KitOfValues


#
class KitOfValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitOfValues
        fields = "__all__"
        # fields = ("value", )

# class KitOfValuesSerializer(serializers.Serializer):
#     # simple serializer for Tag
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=254)
#
#     # queryset = Tag.objects.all()
#
#     def create(self, validated_data):
#         return Tag.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.save()
#         return instance