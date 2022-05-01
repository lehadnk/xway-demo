from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from framework.dependency_container.application_dependency_container import ApplicationDependencyContainer
from framework.http.serializers.paginator_serializer import PaginatorSerializer


class AbstractView(GenericViewSet):
    module = ''

    def get_facade(self):
        return ApplicationDependencyContainer().get_module(self.module).facade

    def responseSuccess(self, data=None, pagination_data=None, status=200):
        if type(pagination_data) is Paginator:
            pagination_data = PaginatorSerializer().serialize(pagination_data)

        return Response({
            'isSuccess': True,
            'data': data,
            'errorMessage': None,
            'pagination': pagination_data
        }, status=status)

    def responseError(self, message, status=422):
        return Response({
            'isSuccess': False,
            'data': None,
            'errorMessage': message,
            'pagination_data': None
        }, status=status)