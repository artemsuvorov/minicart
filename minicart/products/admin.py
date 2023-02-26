from django.contrib import admin

from products.models import Item, ItemInOrder

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemInOrder)