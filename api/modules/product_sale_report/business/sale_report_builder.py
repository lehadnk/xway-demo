from typing import List, Dict

from api.modules.product.dto.product import Product
from api.modules.product.dto.product_list_request import ProductListRequest
from api.modules.product.product_facade import ProductFacade
from api.modules.product_sale_report.dto.product_sale_report_item import ProductSaleReportItem
from api.modules.product_sale_report.dto.product_sale_report_list import ProductSaleReportList
from api.modules.sales.sales_facade import SalesFacade


class SaleReportBuilder:
    def __init__(
            self,
            product_facade: ProductFacade,
            sales_facade: SalesFacade
    ):
        self.product_facade: ProductFacade = product_facade
        self.sales_facade: SalesFacade = sales_facade

    def build_report(self, request: ProductListRequest) -> ProductSaleReportList:
        product_list = self.product_facade.get_product_list(request)
        product_sales = self.get_sales(product_list)

        return self.map_product_list_to_sales(product_list, product_sales)

    def get_products(self, request) -> List[Product]:
        return self.product_facade.get_product_list(request)

    def get_sales(self, product_list: List[Product]):
        request = []
        for product in product_list:
            request.append(product.id)

        return self.sales_facade.get_product_sales(request)

    def map_product_list_to_sales(self, product_list: List[Product], product_sales: Dict) -> ProductSaleReportList:
        result = ProductSaleReportList()
        for product in product_list:
            item = ProductSaleReportItem()
            item.product = product

            if product_sales.get(product.id):
                item.sales = product_sales.get(product.id)
            else:
                item.sales = 0

            result.items.append(item)

        return result