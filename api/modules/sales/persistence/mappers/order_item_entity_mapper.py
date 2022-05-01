from api.modules.sales.dto.order_item import OrderItem
from api.modules.sales.persistence.models.order_item_entity import OrderItemEntity


class OrderItemEntityMapper:
    def map(self, entity: OrderItemEntity, dto: OrderItem) -> OrderItem:
        dto.id = entity.id
        dto.product_id = entity.product_id
        dto.quantity = entity.quantity
        return dto