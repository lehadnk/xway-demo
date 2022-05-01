from typing import Optional, List

from api.modules.product.dto.product import Product
from api.modules.product.dto.product_list_request import ProductListRequest
from api.modules.product.persistence.mappers.product_mapper import ProductMapper
from api.modules.product.persistence.models.product_entity import ProductEntity
from api.modules.product.persistence.product_query_builder import ProductQueryBuilder


class ProductRepository:
    def get_product(self, id: int) -> Optional[Product]:
        try:
            entity = ProductEntity.objects.get(id=id)
            return self.__get_product_mapper().map(entity, Product())
        except:
            return None

    def get_product_list(self, request: ProductListRequest) -> List[Product]:
        query_builder = ProductQueryBuilder()

        queryset = ProductEntity.objects
        queryset = query_builder.enrich_product_list_query(queryset, request)

        entities = queryset.all()

        result = []
        for entity in entities:
            result.append(
                self.__get_product_mapper().map(entity, Product())
            )

        return result

    def __get_product_mapper(self):
        return ProductMapper()