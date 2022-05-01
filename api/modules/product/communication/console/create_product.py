from api.modules.product.dto.create_product_request import CreateProductRequest
from framework.cli.abstract_command import AbstractCommand


class Command(AbstractCommand):
    module = 'product'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--price', dest='price')
        parser.add_argument('-n', '--name', dest='name')

    def handle(self, *args, **options):
        name = options.get('name')
        price = options.get('price')

        request = CreateProductRequest()
        request.name = name
        request.price = price

        self.get_facade().create_product(request)