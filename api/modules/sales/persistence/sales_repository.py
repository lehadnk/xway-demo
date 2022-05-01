from typing import List

from django.db.models import Sum

from api.modules.sales.persistence.mappers.product_sales_mapper import ProductSalesMapper
from api.modules.sales.persistence.models.order_item_entity import OrderItemEntity
from framework.repository.abstract_repository import AbstractRepository


class SalesRepository(AbstractRepository):
    def get_product_sales(self, product_ids: List[int]) -> dict:
        result = OrderItemEntity.objects.filter(product_id__in=product_ids).values('product_id').annotate(sales=Sum('quantity'))
        mapper = ProductSalesMapper()
        return mapper.map(result)
