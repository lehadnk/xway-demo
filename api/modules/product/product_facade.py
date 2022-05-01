from typing import List

from api.modules.product.dto.create_product_request import CreateProductRequest
from api.modules.product.dto.product import Product
from api.modules.product.dto.product_list_request import ProductListRequest
from framework.module.abstract_service_facade import AbstractServiceFacade


class ProductFacade(AbstractServiceFacade):
    def get_product(self, id: int) -> Product:
        return self.get_repository().get_product(id)

    def get_product_list(self, product_list_request: ProductListRequest) -> List[Product]:
        return self.get_repository().get_product_list(product_list_request)

    def create_product(self, request: CreateProductRequest):
        return self.get_entity_manager().create_product(request)