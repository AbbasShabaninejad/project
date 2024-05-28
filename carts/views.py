# region old
# from django.shortcuts import render

# from rest_framework import viewsets, permissions
# from .models import Cart, CartItem
# from .serializers import CartSerializer, CartItemSerializer

# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class CartItemViewSet(viewsets.ModelViewSet):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return CartItem.objects.filter(cart__user=self.request.user)

#     def perform_create(self, serializer):
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         serializer.save(cart=cart)
# endregion

# views.py
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from .serializers import CartItemSerializer

class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        cart = request.session.get('cart', {})
        items = []
        for product_id, item in cart.items():
            items.append({
                'product_id': product_id,
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity']
            })
        total_price = sum(float(item['price']) * item['quantity'] for item in items)
        return Response({'items': items, 'total_price': total_price})

    def add(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            cart[str(pk)]['quantity'] += 1
        else:
            cart[str(pk)] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': 1
            }

        request.session['cart'] = cart
        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)

    def remove(self, request, pk=None):
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart
            return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)
        return Response({'error': 'Product not in cart'}, status=status.HTTP_400_BAD_REQUEST)

