from datetime import datetime
import json
import logging
import random
import requests
import time
from lxml import html

from django.core.management import BaseCommand

from application.apps.stock_resource.models import Stock
from application.apps.stock_resource.models import StockSerieItem

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Gets stock resources"

    def handle(self, *args, **options):
        logger.info("Getting resources")
        stocks = Stock.objects.all()
        for stock in stocks:
            interval_request = random.randrange(2000, 3000)/1000
            time.sleep(interval_request)

            if '{}' in stock.site.url:
                url = stock.site.url.format(stock.name)
            else:
                url = stock.site.url + stock.name

            try:            
                logger.info(f"Accessing {stock.name} resources...")
                page = requests.get(url)

                if page.status_code not in (200, 201):
                    logger.info(f"Content from {stock.name} denied")
                content = page.content
            except:
                content = '<html></html>'

            tree = html.fromstring(content)
            values = {}

            for resource in stock.site.resources.all().order_by('sequence'):
                res = tree.xpath(resource.xpath)
                values[resource.label] = res[0].strip() if res else ''

            stock.resources_value = values
            stock.save()
            datenow = datetime.now()

            if not stock.stock_serie_items.filter(**{
                'create_date__year': datenow.year,
                'create_date__month': datenow.month,
                'create_date__day': datenow.day,
            }):

                StockSerieItem.objects.create(**{
                    'resources_value': stock.resources_value,
                    'stock': stock
                })
