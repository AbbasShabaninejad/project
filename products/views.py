from rest_framework import viewsets, permissions
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        price = product.price
        discount_code = product.discount_code
        if discount_code == 'YOUR_DISCOUNT_CODE':
            # اعمال تخفیف
            price *= 0.9  # 10% تخفیف
        return Response({'name': product.name, 'price': price})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.AllowAny]
