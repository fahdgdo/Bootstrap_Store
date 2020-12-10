from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, clear_cart

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
]
