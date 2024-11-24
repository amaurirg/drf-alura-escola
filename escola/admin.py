from django.contrib import admin
from django.contrib.admin import register
from escola.models import Estudante, Curso, Matricula


@register(Estudante)
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)


@register(Curso)
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)


@register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso')
    list_display_links = ('id', 'estudante')
    search_fields = ('estudante__nome', 'curso__descricao')
