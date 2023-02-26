from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, JsonResponse

import stripe
from stripeapi.session import create_stripe_session

from orders.models import Item, ItemInOrder


stripe.api_key = settings.STRIPE_SECRET_KEY


# TODO: create separate class
def display_cart(request):
    order, context = None, None
    if request.user.is_authenticated:
        user = request.user
        order = ItemInOrder.get_order_or_default(user)
    if order:
        context = {
            'items': order.items,
            'total_price': order.get_display_price()
        }
    return render(request, 'cart.html', context)


@login_required
def buy_order(request):
    user = request.user
    order = ItemInOrder.get_order_or_default(user)

    session = create_stripe_session(
        items=order.items,
        success_url=f'http://{request.get_host()}/success',
        cancel_url=f'http://{request.get_host()}/cart'
    )

    return JsonResponse({
        'id': session.id
    })


@login_required
def add_item_to_cart(request, id):
    user = request.user
    item = Item.find_or_default(id)
    ItemInOrder.objects.create(user=user, item=item)
    return HttpResponse(status=200)