from django.contrib import admin
from catalog.models import Item, ItemDetail, ItemImage


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass
