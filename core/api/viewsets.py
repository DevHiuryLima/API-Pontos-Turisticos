from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]  # Colocando assim passo o token no Header como na vídeo aula.
    # authentication_classes = [BasicAuthentication]  # Usando assim no Insomnia ou postman tenho que ir pelo "Basic Auth"
                                                        # e colocar o login e senha do usuário.

    search_fields = ['nome', 'descricao', 'endereco__linha1']
    lookup_field = 'id'  # Significa que esse é o campo que gostaria que fosse o campo de busca ao invés do 'id'.
                            # esse campo tem que ser exclusivo e unique. Não pode ter dois valores iguais.
                            # Exemplo, se colocar 'nome' e tiver vários dados na tabel com nomes iguais vai dar erro.

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        # Posso fazer qualque tratamento antes.
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # É o GET porém para buscar apenas um objeto. Devo usar ele para buscar
                                                    # um objeto apenas e o 'list' para uma lista de objetos.
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):  # refere-se ao PATCH.
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('Ok')
