from api.modules.sales.dto.order import Order


class OrderPlaceResponse:
    def __init__(self):
        self.is_success: bool
        self.error_message: str
        self.order: Order