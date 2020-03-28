from application.apps.stock_resource.models import Site
from application.apps.stock_resource.models import Resource
from application.apps.stock_resource.models import Stock

from django.contrib import admin

admin.site.register(Site)
admin.site.register(Resource)
admin.site.register(Stock)
