import re
from validate_docbr import CPF


def cpf_invalido(num_cpf):
    # vamos usar a lib validate-docbr
    # return not len(cpf) == 11
    cpf = CPF(num_cpf)
    cpf_valido = cpf.validate(num_cpf)
    return not cpf_valido


def nome_invalido(nome):
    return not nome.isalpha()


def celular_invalido(celular):
    # vamos melhorar essa validação com regex abaixo
    # return not len(celular) == 13

    # padrão ==> XX XXXXX-XXXX
    modelo = r'\d{2} \d{5}-\d{4}'
    resposta = re.findall(modelo, celular)
    return not len(celular) == 13 or not resposta
