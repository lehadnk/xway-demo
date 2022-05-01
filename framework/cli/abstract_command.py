from django.core.management import BaseCommand

from framework.dependency_container.application_dependency_container import ApplicationDependencyContainer
from framework.module.abstract_service_facade import AbstractServiceFacade


class AbstractCommand(BaseCommand):
    module = None

    def get_facade(self) -> AbstractServiceFacade:
        return ApplicationDependencyContainer().get_module(self.module).facade

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    # def add_arguments(self, parser):
    #     super(AbstractCommand, self).add_arguments(parser)
    #
    # def handle(self, *args, **options):
    #     pass