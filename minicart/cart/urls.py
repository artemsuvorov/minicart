from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('item/<int:id>', views.get_item),
    path('buy/<int:id>', views.buy_item),
]