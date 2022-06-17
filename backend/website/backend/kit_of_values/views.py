from django.shortcuts import render
from rest_framework import viewsets

from .serializers import KitSerializer, Kit, KitSerializer_v2


class KitViewSet(viewsets.ModelViewSet):
    queryset = Kit.objects.all()
    # serializer_class = KitSerializer
    serializer_class = KitSerializer_v2

    def get_queryset(self):
        items = Kit.objects.all()
        for item in items:
            # print(item.get_value())
            print(item , item.get_value())
        return items
