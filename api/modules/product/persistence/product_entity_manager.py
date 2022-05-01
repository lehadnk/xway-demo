from api.modules.product.dto.create_product_request import CreateProductRequest
from api.modules.product.persistence.models.product_entity import ProductEntity
from framework.entity_manager.abstract_entity_manager import AbstractEntityManager


class ProductEntityManager(AbstractEntityManager):
    def create_product(self, request: CreateProductRequest):
        ProductEntity.objects.create(
            name=request.name,
            price=request.price
        )