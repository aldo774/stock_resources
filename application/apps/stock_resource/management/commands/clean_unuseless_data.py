from django.core.management import BaseCommand

from application.apps.stock_resource.models import StockSerieItem


class Command(BaseCommand):
    help = "Clean unuseless data"

    def handle(self, *args, **options):
        stocks = StockSerieItem.objects.filter(resources_value__contains={"last-price": ""})
        stocks.delete()
