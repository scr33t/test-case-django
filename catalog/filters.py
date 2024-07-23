from django_filters import FilterSet

from catalog.models import Item


class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = ["title"]
