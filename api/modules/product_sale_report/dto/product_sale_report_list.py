from typing import List

from api.modules.product_sale_report.dto.product_sale_report_item import ProductSaleReportItem


class ProductSaleReportList:
    def __init__(self):
        self.items: List[ProductSaleReportItem] = []