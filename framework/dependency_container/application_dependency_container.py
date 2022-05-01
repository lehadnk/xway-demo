from typing import Dict

from framework.dependency_container.application_dependency_provider import ApplicationDependencyProvider
from framework.service_locator.dto.module import Module


class ApplicationDependencyContainer:
    modules: Dict[str, Module] = {}
    dependency_provider: ApplicationDependencyProvider

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ApplicationDependencyContainer, cls).__new__(cls, *args, **kwargs)
            cls._instance.init()

        return cls._instance

    def init(self):
        provider = ApplicationDependencyProvider()
        for key, module in provider.provide_dependencies(self).items():
            self.modules[key] = module

    def get_module(self, name: str) -> Module:
        if not self.modules.get(name):
            raise Exception(f"No module found: {name}")

        return self.modules[name]
