from typing import List

from api.modules.sales.dto.order_item import OrderItem


class OrderPlaceRequest:
    def __init__(self):
        self.order_items: List[OrderItem] = []