from django.urls import path

from shop import views

urlpatterns = [
    path('item/<int:id>', views.get_item, name='get-item'),
    path('buy/<int:id>', views.buy_item, name='buy-item'),
    path('cancel', views.CancelView.as_view(), name='cancel'),
    path('success', views.SuccessView.as_view(), name='success'),
    path('webhook/stripe', views.my_webhook_view, name='stripe-webhook'),
    path('create-payment-intent/<int:id>', views.StripeIntentView.as_view(), name='create-payment-intent'),
]
