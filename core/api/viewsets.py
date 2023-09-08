from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontoTuristico.objects.all()  # posso mudar o all() por filter(aprovado-True) mas não é recomandado fazer
                                             # esse filtro aqui. Pois pode haver filtragem mais complexa.
    serializer_class = PontoTuristicoSerializer

    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)
    #
    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):  # É o GET porém para buscar apenas um objeto. Devo usar ele para buscar
    #                                                 # um objeto apenas e o 'list' para uma lista de objetos.
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):  # refere-se ao PATCH.
    #     pass
    #
    # @action(methods=['post', 'get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
    #
    # @action(methods=['get'], detail=False)
    # def teste(self, request):
    #     pass
