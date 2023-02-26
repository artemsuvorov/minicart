from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('buy/<int:id>', views.buy_item),
    path('item/<int:id>', views.display_item),
    path('items', views.display_items),

    path('login', LoginView.as_view(template_name='login.html')),
    path('logout', LogoutView.as_view()),
]