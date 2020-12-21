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


def obter_posicoes_adjacentes(pos):
    resultado = ()
    c, l = obter_pos_c(pos), obter_pos_l(pos)
    # obter acima e abaixo
    if l != '1':
        resultado += (cria_posicao(c, str(int(l) - 1)),)
    if l != '3':
        resultado += (cria_posicao(c, str(int(l) + 1)),)
    # obter ah esquerda e direita
    if c != 'a':
        print(chr(ord(c) - 1))
        resultado += (cria_posicao(chr(ord(c) - 1), l),)
    if c != 'c':
        resultado += (cria_posicao(chr(ord(c) + 1), l),)
    # obter centro
    if c in 'ac' and l in '13':  # if eh canto
        resultado += (cria_posicao('b', '2'),)
    # obter cantos
    if c == 'b' and l == '2':
        resultado += tuple(cria_posicao(col, lin)
                           for col in 'ac' for lin in '13')

    return tuple(sorted(resultado,
                        key=lambda x: obter_pos_l(x) + obter_pos_c(x)))
