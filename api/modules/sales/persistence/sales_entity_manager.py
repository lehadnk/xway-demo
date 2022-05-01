from api.modules.sales.dto.order import Order
from api.modules.sales.dto.order_item import OrderItem
from api.modules.sales.persistence.mappers.order_entity_mapper import OrderEntityMapper
from api.modules.sales.persistence.mappers.order_item_entity_mapper import OrderItemEntityMapper
from api.modules.sales.persistence.models.order_entity import OrderEntity
from api.modules.sales.persistence.models.order_item_entity import OrderItemEntity
from framework.entity_manager.abstract_entity_manager import AbstractEntityManager


class SalesEntityManager(AbstractEntityManager):
    def create_order(self) -> Order:
        entity = OrderEntity.objects.create()
        mapper = OrderEntityMapper()

        return mapper.map(entity, Order())

    def create_order_item(self, order_id: int, product_id: int, quantity: int) -> OrderItem:
        entity = OrderItemEntity.objects.create(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity
        )

        mapper = OrderItemEntityMapper()
        return mapper.map(entity, OrderItem())