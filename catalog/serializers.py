from rest_framework.serializers import ModelSerializer

from catalog.models import Item, ItemDetail, ItemImage


class ItemDetailSerializer(ModelSerializer):
    class Meta:
        model = ItemDetail
        fields = ["id", "title", "value", "price", "order"]


class ItemImageSerializer(ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ["id", "image", "caption", "order"]


class ItemListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "description", "price", "order"]


class ItemRetrieveSerializer(ModelSerializer):
    image = ItemImageSerializer()
    details = ItemDetailSerializer()

    class Meta:
        model = Item
        fields = ItemListSerializer.Meta.fields + ["image", "details"]
