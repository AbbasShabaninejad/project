# from django.urls import path, include
# from . import views
# # for viewset
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('',views.ProductViewSetApiView)


# urlpatterns = [
#     # path('',views.product_json)
#     path('',views.all_product),
#     path('<int:product_id>',views.product_detail_view),
#     path('cbv',views.ManageProductApiView.as_view()),
#     path('cbv/<int:pk>',views.ProductDetailApiView.as_view()),
#     path('mixins/',views.ProductListMixinApiView.as_view()),
#     path('mixins/<pk>',views.ProductDetailtMixinApiView.as_view()),
#     path('generics/',views.ProductGenericApiView.as_view()),
#     path('generics/<pk>',views.ProductGenericDetailApiView.as_view()),
#     path('viewsets/',include(router.urls)),
#     # path('users/',views.UserGenericApiView.as_view()),

# ]

# # views.Home.as_view(), name="home"