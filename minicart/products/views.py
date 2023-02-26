from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

import stripe
from stripeapi.session import create_stripe_session

from products.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def buy_item(request, id):
    item = Item.find_or_default(id)
    
    session = create_stripe_session(        
        items=[item],
        success_url=f'http://{request.get_host()}/success',
        cancel_url=f'http://{request.get_host()}/item/{item.id}',
    )

    return JsonResponse({
        'id': session.id
    })


def display_item(request, id):
    item = Item.find_or_default(id)
    return render(request, 'item.html', {
        'item': item
    })


def display_items(request):
    return render(request, 'items.html', {
        'items': Item.get_all_items()
    })