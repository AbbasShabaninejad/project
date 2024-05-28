from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shops.views import ShopViewSet

router = DefaultRouter()
router.register(r'shops', ShopViewSet)

urlpatterns = [
    path('shop/', include(router.urls)),
]
