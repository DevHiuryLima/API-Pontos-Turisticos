from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
