def cpf_invalido(cpf):
    return not len(cpf) == 11


def nome_invalido(nome):
    return not nome.isalpha()


def celular_invalido(celular):
    return not len(celular) == 13
