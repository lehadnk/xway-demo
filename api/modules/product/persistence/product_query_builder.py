from api.modules.product.dto.product_list_request import ProductListRequest


class ProductQueryBuilder:
    def enrich_product_list_query(
            self,
            queryset,
            product_list_request: ProductListRequest
    ):
        return queryset.order_by(product_list_request.order)[product_list_request.offset:product_list_request.offset + product_list_request.limit]