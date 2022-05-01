from framework.entity_manager.abstract_entity_manager import AbstractEntityManager
from framework.repository.abstract_repository import AbstractRepository
from framework.service_locator.dto.module import Module


class AbstractServiceFactory:
    def __init__(
            self,
            dependency_container,
            repository: AbstractRepository = None,
            entity_manager: AbstractEntityManager = None
    ):
        self.dependency_container = dependency_container
        self.repository = repository
        self.entity_manager = entity_manager

    def get_repository(self):
        if not self.repository:
            raise Exception(f"No repository found in service")

        return self.repository

    def get_entity_manager(self) -> AbstractEntityManager:
        if not self.entity_manager:
            raise Exception("No entity manager defined for facade")

        return self.entity_manager

    def provide_module(self, module_name: str) -> Module:
        return self.dependency_container.get_module(module_name)