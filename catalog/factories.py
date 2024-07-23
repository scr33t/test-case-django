import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from catalog.models import Item, ItemDetail, ItemImage


class ItemImageFactory(DjangoModelFactory):
    class Meta:
        model = ItemImage

    image = factory.django.ImageField()
    caption = fuzzy.FuzzyText()
    order = fuzzy.FuzzyInteger(0, 100)


class ItemDetailFactory(DjangoModelFactory):
    class Meta:
        model = ItemDetail

    title = fuzzy.FuzzyText()
    value = fuzzy.FuzzyText()
    price = fuzzy.FuzzyInteger(100, 1000)
    order = fuzzy.FuzzyInteger(0, 100)


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    title = fuzzy.FuzzyText()
    description = fuzzy.FuzzyText()
    price = fuzzy.FuzzyInteger(100, 1000)
    order = fuzzy.FuzzyInteger(0, 100)
    image = factory.SubFactory(ItemImageFactory)
    details = factory.SubFactory(ItemDetailFactory)
