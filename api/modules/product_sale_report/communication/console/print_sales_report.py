from api.modules.product.dto.create_product_request import CreateProductRequest
from api.modules.product.dto.product_list_request import ProductListRequest
from framework.cli.abstract_command import AbstractCommand


class Command(AbstractCommand):
    module = 'product_sale_report'

    def handle(self, *args, **options):
        request = ProductListRequest()
        report = self.get_facade().get_sale_report(request)

        for item in report.items:
            print(f"{item.product.name}: {item.sales}")
