from typing import List

from api.modules.sales.dto.order_item import OrderItem


class Order:
    def __init__(self):
        self.id: int
        self.order_items: List[OrderItem] = []

        # customer
        self.customer_data = []