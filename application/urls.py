from application.apps.drf.v1.views import get_stock
from application.apps.drf.v1.views import get_stocks_serie
from application.apps.drf.v1.views import get_stocks
from application.apps.drf.v1.views import post_stocks

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/get_stocks/', get_stocks),
    path('api/v1/get_stock/<str:stock>/', get_stock),
    path('api/v1/get_stocks_serie/<str:stocks>/', get_stocks_serie),
    path('api/v1/post_stocks/', post_stocks),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
