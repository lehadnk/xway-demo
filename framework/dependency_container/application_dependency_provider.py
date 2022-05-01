from typing import Dict, Type

from api.modules.product.persistence.product_entity_manager import ProductEntityManager
from api.modules.product.persistence.product_repository import ProductRepository
from api.modules.product.product_facade import ProductFacade
from api.modules.product_sale_report.product_sale_report_facade import ProductSaleReportFacade
from api.modules.product_sale_report.product_sale_report_factory import ProductSaleReportFactory
from api.modules.sales.persistence.sales_entity_manager import SalesEntityManager
from api.modules.sales.persistence.sales_repository import SalesRepository
from api.modules.sales.sales_facade import SalesFacade
from api.modules.sales.sales_factory import SalesFactory
from framework.service_locator.dto.module import Module


class ApplicationDependencyProvider:
    def provide_dependencies(self, container) -> Dict[str, Module]:
        return {
            "product": Module(
                container,
                facade_class=ProductFacade,
                repository_class=ProductRepository,
                entity_manager_class=ProductEntityManager,
            ),
            "sales": Module(
                container,
                facade_class=SalesFacade,
                factory_class=SalesFactory,
                entity_manager_class=SalesEntityManager,
                repository_class=SalesRepository,
            ),
            "product_sale_report": Module(
                container,
                facade_class=ProductSaleReportFacade,
                factory_class=ProductSaleReportFactory,
            )
        }