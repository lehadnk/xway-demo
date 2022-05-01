from typing import List

from api.modules.sales.dto.order_place_request import OrderPlaceRequest
from api.modules.sales.dto.order_place_response import OrderPlaceResponse
from framework.module.abstract_service_facade import AbstractServiceFacade


class SalesFacade(AbstractServiceFacade):
    def place_order(self, request: OrderPlaceRequest) -> OrderPlaceResponse:
        return self.get_factory().create_order_handler().place_order(request)

    def get_product_sales(self, product_ids: List[int]) -> dict:
        return self.get_factory().get_repository().get_product_sales(product_ids)
