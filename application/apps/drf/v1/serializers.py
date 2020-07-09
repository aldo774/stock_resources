from application.apps.stock_resource.models import Site
from application.apps.stock_resource.models import Resource
from application.apps.stock_resource.models import Stock
from application.apps.stock_resource.models import StockSerieItem

from rest_framework import serializers


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class StockSerieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSerieItem
        fields = "__all__"