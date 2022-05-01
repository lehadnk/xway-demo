from api.modules.sales.dto.order import Order
from api.modules.sales.persistence.models.order_entity import OrderEntity


class OrderEntityMapper:
    def map(self, entity: OrderEntity, dto: Order) -> Order:
        dto.id = entity.id
        return dto