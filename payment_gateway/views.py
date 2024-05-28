from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def process_payment(request):
    # دریافت مقدار مبلغ از درخواست
    amount = request.data.get('amount')

    try:
        # ایجاد تراکنش در Stripe
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=request.data.get('token'),
            description='Payment for cart items'
        )

        # در صورت موفقیت‌آمیز بودن تراکنش، مقادیر سبد خرید را به‌روزرسانی کنید
        cart.update(items=[], total_amount=0)

        return Response({'success': True, 'message': 'Payment processed successfully'})
    except stripe.error.CardError as e:
        # اگر خطای کارت رخ داد، پیام مربوطه را برگردانید
        return Response({'success': False, 'error': str(e)})
