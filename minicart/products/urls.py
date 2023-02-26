from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views, cart


urlpatterns = [
    path('', views.index),

    path('success', views.success),

    path('buy/<int:id>', views.buy_item),
    path('item/<int:id>', views.display_item),

    path('items', views.display_items),

    path('cart', cart.display_cart),
    path('cart/add/<int:id>', cart.add_item_to_cart),

    path('order', cart.buy_order),

    path('login', LoginView.as_view(template_name='login.html')),
    path('logout', LogoutView.as_view()),
]