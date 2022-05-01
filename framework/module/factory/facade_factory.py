class FacadeFactory:
    def build(self, facade_class, factory_class):
        return facade_class(factory_class)