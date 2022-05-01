from typing import Type

# from framework.entity_manager.abstract_entity_manager import AbstractEntityManager
# from framework.module.abstract_service_facade import AbstractServiceFacade
# from framework.module.abstract_service_factory import AbstractServiceFactory
# from framework.repository.abstract_repository import AbstractRepository


class Module:
    def __init__(
            self,
            dependency_container,
            facade_class: Type,
            factory_class: Type = None,
            repository_class: Type = None,
            entity_manager_class: Type = None
    ):
        self.repository = None
        self.entity_manager = None
        self.factory = None
        if repository_class:
            self.repository = repository_class()

        if entity_manager_class:
            self.entity_manager = entity_manager_class()

        if factory_class:
            self.factory = factory_class(
                dependency_container=dependency_container,
                repository=self.repository,
                entity_manager=self.entity_manager
            )

        self.facade = facade_class(
            factory=self.factory,
            repository=self.repository,
            entity_manager=self.entity_manager
        )