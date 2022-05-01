class GetProductWorker:
    def run(self, id: int):
        celery.run_task({id: id})

    def handle(self, data):
        id = data.id
        self.get_facade().get_product(id)