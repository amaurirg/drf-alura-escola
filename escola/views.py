# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer, CursoSerializer, MatriculaSerializer,
    ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer, EstudanteSerializerV2
)
# Como inserimos no settings o REST_FRAMEWORK = {...}, não precisamos dessas configurações dentro de cada view
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class EstudanteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # sem a lib django-filters
    # queryset = Estudante.objects.all().order_by('nome')

    # com a lib django-filters (indicado pela doc do drf)
    # colocando order_by não recebemos a msg do servidor sobre 'dados não ordenados'
    queryset = Estudante.objects.all().order_by('id')
    # usamos get_serializer_class para verificar através da versão, qual serializer usar
    # serializer_class = EstudanteSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer



class CursoViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset = Curso.objects.all().order_by('descricao')
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer


# Criamos uma nova classe sobrescrevendo AnonRateThrottle para
# mudar a quantidade de requisições/dia (configurada no settings)
class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'


class MatriculaViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    # queryset = Matricula.objects.all().order_by('periodo')
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    # permissão diferente do padrão configurada no settings
    throttle_classes = [MatriculaAnonRateThrottle, UserRateThrottle]


class ListaMatriculaEstudante(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
