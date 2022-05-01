from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class OrderItemEntity(TimeStampedModel):
    order = models.ForeignKey('api.OrderEntity', on_delete=models.CASCADE)
    product = models.ForeignKey('api.ProductEntity', on_delete=models.CASCADE)
    quantity = models.IntegerField(_('Quantity'))

    class Meta:
        db_table = 'order_items'
        app_label = 'api'
