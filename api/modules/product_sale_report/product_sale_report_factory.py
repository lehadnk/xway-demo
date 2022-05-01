from api.modules.product_sale_report.business.sale_report_builder import SaleReportBuilder
from framework.module.abstract_service_factory import AbstractServiceFactory


class ProductSaleReportFactory(AbstractServiceFactory):
    def create_sale_report_builder(self):
        return SaleReportBuilder(
            self.provide_module('product').facade,
            self.provide_module('sales').facade
        )