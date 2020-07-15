from django.core.management import BaseCommand

from application.apps.stock_resource.models import StockSerieItem


class Command(BaseCommand):
    help = "Clean unuseless data"

    def turning_float(self, value):
        try:
            string_float = value.replace(",", ".").replace("%", "")
            return float(string_float)
        except ValueError:
            return value

    def handle(self, *args, **options):
        stocks = StockSerieItem.objects.all()
        resource_keys = [
            "roic", 
            "dy", 
            "cres-rec-5a", 
            "marg-bruta", 
            "marg-liq", 
            "ebit/ativo", 
            "roe"
        ]
        resource_value = {}
        for stock in stocks:
            for key, value in stock.resources_value.items():
                new_value = self.turning_float(value)
                new_key = key
                if key in resource_keys:
                    new_key += "(%)"
                resource_value[new_key] = new_value
            stock.resources_value = resource_value
            stock.save()
