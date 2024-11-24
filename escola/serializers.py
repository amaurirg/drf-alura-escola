from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    # Ao invés de fazermos uma validação pra cada campo, faremos somente 1 validate para todos
    # def validate_cpf(self, cpf):
    #     if not len(cpf) == 11:
    #         raise serializers.ValidationError('O CPF deve ter 11 digitos!')
    #     return cpf
    #
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError('O nome deve ter apenas letras!')
    #     return nome
    #
    # def validate_celular(self, celular):
    #     if not len(celular) == 13:
    #         raise serializers.ValidationError('O celular deve ter 13 digitos!')
    #     return celular

    # com apenas 1 validate
    # def validate(self, data):
    #     if not len(data['cpf']) == 11:
    #         raise serializers.ValidationError({'cpf': 'O CPF deve ter 11 digitos!'})
    #     if not data['nome'].isalpha():
    #         raise serializers.ValidationError({'nome': 'O nome deve ter apenas letras!'})
    #     if not len(data['celular']) == 13:
    #         raise serializers.ValidationError({'celular': 'O celular deve ter 13 digitos!'})
    #     return data

    # separando em um arquivo validators.py
    def validate(self, data):
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ter um valor válido!'})
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome': 'O nome deve ter apenas letras!'})
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve ter 13 digitos no formato XX XXXXX-XXXX!'})
        return data


class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'celular']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
