from api.modules.sales.dto.order_place_request import OrderPlaceRequest
from api.modules.sales.dto.order_place_response import OrderPlaceResponse
from api.modules.sales.persistence.sales_entity_manager import SalesEntityManager


class OrderHandler:
    def __init__(
            self,
            sales_entity_manager: SalesEntityManager
    ):
        self.sales_entity_manager = sales_entity_manager

    def place_order(self, request: OrderPlaceRequest) -> OrderPlaceResponse:
        order = self.sales_entity_manager.create_order()
        for order_item in request.order_items:
            order_item = self.sales_entity_manager.create_order_item(order.id, order_item.product_id, order_item.quantity)
            order.order_items.append(order_item)

        response = OrderPlaceResponse()
        response.is_success = True
        response.order = order
        return response