from api.modules.product.dto.product import Product


class ProductSaleReportItem:
    def __init__(self):
        self.product: Product
        self.sales: int