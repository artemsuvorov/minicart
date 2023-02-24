from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse

import stripe

# from products.models import items
from products.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def buy_item(request, id):
    item = _find_item_or_default(id)
    
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': { 
                    'currency': 'USD',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'unit_amount': item.price
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'http://{request.get_host()}/success',
        cancel_url=f'http://{request.get_host()}/item/{item.id}',
    )

    return JsonResponse({
        'id': session.id
    })


def get_item(request, id):
    item = _find_item_or_default(id)
    return render(request, 'item.html', {
        'item': item
    })


def _find_item_or_default(id):
    return Item.objects.get(id=id)
    # valid_id = id >= 0 and id < len(items)
    # return items[id] if valid_id else None