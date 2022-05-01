from framework.entity_manager.abstract_entity_manager import AbstractEntityManager
from framework.module.abstract_service_factory import AbstractServiceFactory
from framework.repository.abstract_repository import AbstractRepository


class AbstractServiceFacade:
    factory: AbstractServiceFactory

    def __init__(
            self,
            factory: AbstractServiceFactory = None,
            repository: AbstractRepository = None,
            entity_manager: AbstractEntityManager = None
    ):
        self.factory = factory
        self.repository = repository
        self.entity_manager = entity_manager

    def get_factory(self) -> AbstractServiceFactory:
        if not self.factory:
            raise Exception("No factory defined for facade")

        return self.factory

    def get_repository(self) -> AbstractRepository:
        if not self.repository:
            raise Exception("No repository defined for facade")

        return self.repository

    def get_entity_manager(self) -> AbstractEntityManager:
        if not self.entity_manager:
            raise Exception("No entity manager defined for facade")

        return self.entity_manager
