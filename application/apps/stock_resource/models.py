import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class StandardModelMixin(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Id")

    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at")

    write_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at")

    class Meta:
        abstract = True


class Site(StandardModelMixin):
    name = models.CharField(max_length=20)
    url = models.TextField()

    def __str__(self):
        return self.name


class Resource(StandardModelMixin):
    xpath = models.TextField()
    label = models.CharField(max_length=100)
    sequence = models.IntegerField(blank=True)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='resources'
    )
    xpath = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.label, self.site.name)


class Stock(StandardModelMixin):
    name = models.CharField(max_length=10)
    resources_value = JSONField(blank=True)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='stocks'
    )

    def __str__(self):
        return '%s - %s' % (self.name, self.site.name)


class StockSerieItem(StandardModelMixin):
    resources_value = JSONField(blank=True)
    stock = models.ForeignKey(
        Stock,
        on_delete= models.CASCADE,
        related_name='stock_serie_items'
    )

    def __str__(self):
        return '%s - %s' % (self.stock.name, self.create_date)
