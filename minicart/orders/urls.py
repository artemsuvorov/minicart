from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('cart', views.display_cart),
    path('cart/add/<int:id>', views.add_item_to_cart),

    path('order', views.buy_order),
]