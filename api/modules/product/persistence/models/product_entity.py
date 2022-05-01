from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class ProductEntity(TimeStampedModel):
    name = models.CharField(_('Name'), null=False, max_length=150)
    price = models.IntegerField(_('Price'), null=False)

    class Meta:
        db_table = 'products'
        app_label = 'api'
