from rest_framework.routers import DefaultRouter

from catalog.api import ItemViewSet

router = DefaultRouter()


router.register(r"items", ItemViewSet)
