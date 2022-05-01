from api.modules.product.communication.http.serializers.product_serializer import ProductSerializer
from api.modules.product.dto.product_list_request import ProductListRequest
from framework.http.abstract_view import AbstractView


class ProductView(AbstractView):
    module = 'product'

    def get(self, data: dict, id: int):
        product = self.get_facade().get_product(id)
        if not product:
            return self.responseError("No product found", 404)

        serializer = ProductSerializer(product, many=False)

        return self.responseSuccess(serializer.data)

    def list(self, data: dict):
        product_list_request = ProductListRequest()

        products = self.get_facade().get_product_list(product_list_request)

        serializer = ProductSerializer(products, many=True)

        return self.responseSuccess(serializer.data)