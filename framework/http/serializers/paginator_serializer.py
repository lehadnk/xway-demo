from django.core.paginator import Paginator


class PaginatorSerializer:
    def serialize(self, paginator: Paginator):
        return {
            'count': paginator.count,
            'totalPages': paginator.num_pages,
            'pageSize': paginator.per_page,
        }