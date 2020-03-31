from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=20)
    url = models.TextField()

    def __str__(self):
        return self.name


class Resource(models.Model):
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


class Stock(models.Model):
    name = models.CharField(max_length=10)
    resources_value = models.TextField(blank=True)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='stocks'
    )
    write_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.site.name)


class StockSerieItem(models.Model):
    resources_value = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    stock = models.ForeignKey(
        Stock,
        on_delete= models.CASCADE,
        related_name='stock_serie_items'
    )

    def __str__(self):
        return '%s - %s' % (self.stock.name, self.create_date)
