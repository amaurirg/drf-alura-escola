from rest_framework import viewsets, generics
from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer, CursoSerializer, MatriculaSerializer,
    ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
)
# Como inserimos no settings o REST_FRAMEWORK = {...}, não precisamos dessas configurações dentro de cada view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser


class EstudanteViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculaEstudante(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer
