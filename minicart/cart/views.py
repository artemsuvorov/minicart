from django.shortcuts import render

from cart.models import items


def index(request):
    return render(request, 'index.html')


def buy_item(request):
    raise NotImplementedError()


def get_item(request, id):
    valid_id = id >= 0 and id < len(items)
    item = items[id] if valid_id else None
    return render(request, 'item.html', {
        'item': item
    })