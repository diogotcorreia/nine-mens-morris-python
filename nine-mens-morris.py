# Diogo Torres Correia - ist199211

###############
# TAD Posicao #
###############

def cria_posicao(c, l):
    if type(c) != str or type(l) != str or c not in 'abc' or l not in '123':
        raise ValueError("cria_posicao: argumentos invalidos")
    return {'c': c, 'l': l}


def cria_copia_posicao(pos):
    return {'c': pos['c'], 'l': pos['l']}


def obter_pos_c(pos):
    return pos['c']


def obter_pos_l(pos):
    return pos['l']


def eh_posicao(pos):
    return type(pos) == dict and \
        'c' in pos and \
        'l' in pos and \
        type(pos['c']) == str and \
        type(pos['l']) == str and \
        pos['c'] in 'abc' and \
        pos['l'] in '123'


def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and \
        eh_posicao(p2) and \
        obter_pos_c(p1) == obter_pos_c(p2) and \
        obter_pos_l(p1) == obter_pos_l(p2)


def posicao_para_str(pos):
    return obter_pos_c(pos) + obter_pos_l(pos)
