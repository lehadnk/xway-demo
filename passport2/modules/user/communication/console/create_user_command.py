from django.core.management import BaseCommand


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def handle(self, *args, **options):
        UserServiceFacade
        pass