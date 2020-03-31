import json
import logging
import random
import requests
import time
from lxml import html

from django.core.management import BaseCommand

from application.apps.stock_resource.models import Stock

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
            
            logger.info(f"Accessing {stock.name} resources...")
            page = requests.get(url)

            if page.status_code not in (200, 201):
                logger.info(f"Content from {stock.name} denied")

            tree = html.fromstring(page.content)
            values = {}

            for resource in stock.site.resources.all().order_by('sequence'):
                res = tree.xpath(resource.xpath)
                values[resource.label] = res[0].strip() if res else ''

            stock.resources_value = values
            stock.save()
