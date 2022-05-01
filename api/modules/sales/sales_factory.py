from api.modules.sales.business.order_handler import OrderHandler
from framework.module.abstract_service_factory import AbstractServiceFactory


class SalesFactory(AbstractServiceFactory):
    def create_order_handler(self) -> OrderHandler:
        return OrderHandler(
            self.get_entity_manager()
        )