from rest_framework.viewsets import ModelViewSet

from catalog.models import Item
from catalog.serializers import ItemListSerializer, ItemRetrieveSerializer
from catalog.filters import ItemFilter


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    filterset_class = ItemFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        return ItemRetrieveSerializer
