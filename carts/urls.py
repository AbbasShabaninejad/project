# region old
#  from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CartViewSet, CartItemViewSet
# # from .views import update_cart

# router = DefaultRouter()
# router.register(r'carts', CartViewSet )#, basename='cart'
# router.register(r'cart-items', CartItemViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('update-cart/', update_cart, name='update_cart'),
# ]
# endregion

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
