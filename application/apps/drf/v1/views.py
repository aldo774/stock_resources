import json
from datetime import timedelta

from application.apps.stock_resource.models import Site
from application.apps.stock_resource.models import Resource
from application.apps.stock_resource.models import Stock
from application.apps.stock_resource.models import StockSerieItem
from application.apps.drf.v1.serializers import SiteSerializer
from application.apps.drf.v1.serializers import ResourceSerializer
from application.apps.drf.v1.serializers import StockSerializer
from application.apps.drf.v1.serializers import StockSerieItemSerializer

from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class StandardModelViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class SiteViewSet(StandardModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ResourceViewSet(StandardModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class StockViewSet(StandardModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    http_method_names = ['get', 'post', 'head', 'put', 'patch' 'delete']


@api_view(["GET"])
def get_serie_stocks(request: Request) -> Response:
    filters_query = request.query_params.dict()

    for key, value in filters_query.items():
        if key.startswith("list_"):
            value_list = value.split(",")
            filters_query[f'{key.replace("list_", "")}__in'] = value_list
            del filters_query[key]

    stocks = Stock.objects.filter(**filters_query)
    list_response = []

    for stock in stocks:
        list_response.append({
            "name": stock.name,
            "last_resource": stock.resources_value,
            "serie": [{
                    **s.resources_value,
                    "create_date": s.create_date
                }
                for s in stock.stock_serie_items.filter(**{
                "create_date__gte": timezone.now() - timedelta(days=90),
            }).order_by('create_date')]
        })

    return Response({"result": list_response})


class StockSerieItemViewSet(StandardModelViewSet):
    queryset = StockSerieItem.objects.all()
    serializer_class = StockSerieItemSerializer
