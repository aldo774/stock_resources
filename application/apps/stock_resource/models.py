from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=20)
    url = models.TextField()

    def __str__(self):
        return self.name


class Resource(models.Model):
    xpath = models.TextField()
    label = models.CharField(max_length=100)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='resources'
    )

    def __str__(self):
        return '%s - %s' % (self.label, self.site.name)


class Stock(models.Model):
    name = models.CharField(max_length=10)
    resources_value = models.TextField(blank=True)
    write_date = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(
        Site,
        on_delete= models.CASCADE,
        related_name='stocks'
    )

    def __str__(self):
        return '%s - %s' % (self.name, self.site.name)
