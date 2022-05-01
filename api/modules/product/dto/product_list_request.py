class ProductListRequest:
    def __init__(self):
        self.order: str = 'id'
        self.limit: int = 25
        self.offset: int = 0