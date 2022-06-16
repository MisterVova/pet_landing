from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..serializers import KitOfValuesSerializer, KitOfValues


class KitViewSet(viewsets.ModelViewSet):
    queryset = KitOfValues.objects.all()
    serializer_class = KitOfValuesSerializer
    # permission_classes = (IsAdminUser,)

    def get_queryset(self):
        items = KitOfValues.objects.all()
        for item in items:
            # print(item.get_value())
            print(item , item.get_value())
        return items