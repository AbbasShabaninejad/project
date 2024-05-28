
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from SOUVENIR import settings
# token authentication
from rest_framework.authtoken.views import obtain_auth_token
# swagger
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('products.urls')),
    path('api/',include('shops.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('carts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # Doc swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    #  UI(user interface):
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]
urlpatterns += static(settings.MEDIA_URL, doctest_root=settings.MEDIA_ROOT)
