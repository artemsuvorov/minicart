from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, JsonResponse

import stripe

from products.models import Item, ItemInOrder


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


def create_stripe_session(items, success_url, cancel_url):
    session = stripe.checkout.Session.create(
        line_items=get_line_items(items),
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session


def get_line_items(items):
    items_with_quantity = {
        item : items.count(item) for item in items
    }
    return list(
        {
            'price_data': { 
                'currency': 'USD',
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': item.price
            },
            'quantity': quantity,
        } 
        for item, quantity 
        in items_with_quantity.items()
    )