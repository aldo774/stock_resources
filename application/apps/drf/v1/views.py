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
from rest_framework import viewsets
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


class StockSerieItemViewSet(StandardModelViewSet):
    queryset = StockSerieItem.objects.all()
    serializer_class = StockSerieItemSerializer
