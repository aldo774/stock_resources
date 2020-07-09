from application.apps.drf.v1 import views

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views as drf_auth_views

router = routers.DefaultRouter()

router.register("sites", views.SiteViewSet, basename="sites-view")
router.register("resources", views.ResourceViewSet, basename="resources-view")
router.register("stock", views.StockViewSet, basename="stock-view")
router.register("stock-serie-items", views.StockSerieItemViewSet, basename="stock-serie-items-view")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/auth-token/", drf_auth_views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
