from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('item/<int:id>', views.get_item)
]