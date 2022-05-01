from api.modules.product.dto.product_list_request import ProductListRequest
from api.modules.product_sale_report.dto.product_sale_report_list import ProductSaleReportList
from framework.module.abstract_service_facade import AbstractServiceFacade


class ProductSaleReportFacade(AbstractServiceFacade):
    def get_sale_report(self, request: ProductListRequest) -> ProductSaleReportList:
        return self.get_factory().create_sale_report_builder().build_report(request)