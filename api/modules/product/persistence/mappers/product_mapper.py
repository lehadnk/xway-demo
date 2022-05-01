from api.modules.product.dto.product import Product
from api.modules.product.persistence.models.product_entity import ProductEntity


class ProductMapper:
    def map(self, entity: ProductEntity, dto: Product):
        dto.id = entity.id
        dto.name = entity.name
        dto.price = entity.price
        return dto