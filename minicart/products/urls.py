from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),

    path('success', views.success),

    path('buy/<int:id>', views.buy_item),
    path('item/<int:id>', views.display_item),

    path('items', views.display_items),
]