import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from shop.models import Item

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY


class CancelView(TemplateView):
    template_name = "shop/cancel.html"


class SuccessView(TemplateView):
    template_name = "shop/success.html"


def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'shop/index.html',
                  {"title": "Shop", "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY, "item": item})


def buy_item(request, id):
    item_id = id
    item = Item.objects.get(id=item_id)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price_data': {
                    'currency': item.currency.name,
                    'unit_amount': item.get_stripe_cost(),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    }
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": item.id
        },
        mode='payment',
        success_url=settings.DOMAIN + '/success',
        cancel_url=settings.DOMAIN + '/cancel',
    )
    return JsonResponse(
        {'id': checkout_session.id}
    )


@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )

        line_items = session.line_items
        # Fulfill the purchase...
        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]
        send_mail(
            subject="Here is your product",
            message="Thank you for shopinng.",
            recipient_list=[customer_email],
            from_email="mail@test.com"
        )
    # Passed signature verification
    return HttpResponse(status=200)
