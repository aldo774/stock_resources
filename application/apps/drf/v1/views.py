import json

from application.apps.stock_resource.models import Site
from application.apps.stock_resource.models import Stock

from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_stocks(request):
    stock_info = []
    stocks = Stock.objects.all()
    for stock in stocks:
        stock_info.append({
            'name': stock.name,
            **(json.loads(stock.resources_value)
                if stock.resources_value else {})
        })
    
    return JsonResponse({'data': stock_info})


@api_view(["post"])
def post_stocks(request):
    data = request.data
    stocks = request.data.get('stocks').split(',')
    site_id = request.data.get('site_id')

    for stock in stocks:
        Stock.objects.create(**{
            'name': stock,
            'site': Site.objects.get(id=site_id)
        })

    return JsonResponse({'message': 'ok'})
