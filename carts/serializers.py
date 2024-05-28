# region old
# from rest_framework import serializers
# from .models import Cart, CartItem
# from products.serializers import ProductSerializer
# from products.models import Product

# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#     product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'product_id', 'quantity']

# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'items']
#         read_only_fields = ['user']

# endregion

from rest_framework import serializers

class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()
