from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

class OrderEntity(TimeStampedModel):
    class Meta:
        db_table = 'orders'
        app_label = 'api'