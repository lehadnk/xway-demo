from django.urls import path

from api.modules.product.communication.http.product_view import ProductView
from api.modules.sales.communication.http.place_order_view import PlaceOrderView

app_name = 'pis'

urlpatterns = [
    path('products/<int:id>/', ProductView.as_view({'get': 'get'})),
    path('products/', ProductView.as_view({'get': 'list'})),

    path('orders/', PlaceOrderView.as_view({'post': 'post'})),
]