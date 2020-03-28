import uuid

from django.db import models


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
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='resources'
    )

    def __str__(self):
        return '%s - %s' % (self.label, self.site.name)


class Stock(StandardModelMixin):
    name = models.CharField(max_length=10)
    resources_value = models.TextField(blank=True)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='stocks'
    )

    def __str__(self):
        return '%s - %s' % (self.name, self.site.name)
