import json

from rest_framework.request import Request

from api.modules.sales.dto.order_item import OrderItem
from api.modules.sales.dto.order_place_request import OrderPlaceRequest
from framework.http.abstract_view import AbstractView


class PlaceOrderView(AbstractView):
    module = 'sales'

    def post(self, request: Request):
        data = json.loads(request.body)
        request = OrderPlaceRequest()
        for order_item in data:
            order_item_dto = OrderItem()
            order_item_dto.product_id = order_item.get('product_id')
            order_item_dto.quantity = order_item.get('quantity')

            request.order_items.append(order_item_dto)

        response = self.get_facade().place_order(request)
        if not response.is_success:
            return self.responseError({
                "message": response.error_message
            })

        return self.responseSuccess({
            "order_id": response.order.id
        })
