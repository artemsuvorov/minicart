from django.db import models
from django.contrib.auth.models import User

from products.models import Item


class ItemInOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @staticmethod
    def get_order_or_default(user):
        try:
            items = list(x.item for x in user.iteminorder_set.all())
            return Order(items)
        except ItemInOrder.DoesNotExist:
            return None

    def __str__(self):
        return self.item.name


class Order:
    def __init__(self, items):
        self.items = items
        self.total_price = sum(item.price for item in self.items)

    def get_display_price(self):
        return '{0:.2f}'.format(self.total_price / 100)