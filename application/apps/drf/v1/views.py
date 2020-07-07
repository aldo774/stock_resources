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
                if stock.resources_value else {}),
            'write_date': stock.write_date
        })
    stock_info.sort(key=lambda stock: stock.get('name'))
    
    return JsonResponse({'data': stock_info})


@api_view(["GET"])
def get_stock(request, stock):
    stock_info = []
    stock_rec = Stock.objects.filter(name=stock)[0]
    data = {
        'name': stock_rec.name,
        'write_date': stock_rec.write_date,
        **(json.loads(stock_rec.resources_value)
        if stock_rec.resources_value else {})
    }

    return JsonResponse(data)


@api_view(["GET"])
def get_stocks_serie(request, stocks):
    response = {
        "result": []
    }
    stock_list = stocks.split(",")
    stock_info = []

    for stk in stock_list:
        stock_rec = Stock.objects.filter(name=stk)[0]
        data = {
            'stock': stock_rec.name,
            'serie': [{
                **json.loads(s.resources_value), 
                'create_date': s.create_date
                } for s in stock_rec.stock_serie_items.all()]
        }
        response["result"].append(data)

    return JsonResponse(response)


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
