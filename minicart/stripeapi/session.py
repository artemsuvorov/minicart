import stripe


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