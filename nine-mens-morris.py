# Diogo Torres Correia - ist199211

###############
# TAD Posicao #
###############

def cria_posicao(c, l):
    """
    cria_posicao: str X str -> posicao
    Recebe uma coluna e linha de uma posicao e retorna um
    dicionario que corresponde ah representacao interna da posicao.
    R[c, l] = {'c': c, 'l': l}
    """
    if type(c) != str or type(l) != str or c not in 'abc' or l not in '123':
        raise ValueError("cria_posicao: argumentos invalidos")
    return {'c': c, 'l': l}


def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    Recebe uma posicao e devolve uma copia nova da posicao.
    """
    return {'c': pos['c'], 'l': pos['l']}


def obter_pos_c(pos):
    """
    obter_pos_c: posicao -> str
    Recebe uma posicao e devolve a componente coluna da posicao.
    """
    return pos['c']


def obter_pos_l(pos):
    """
    obter_pos_l: posicao -> str
    Recebe uma posicao e devolve a componente linha da posicao.
    """
    return pos['l']


def eh_posicao(pos):
    """
    eh_posicao: universal -> booleano
    Devolve True caso o seu argumento seja um TAD posicao
    e False caso contrario.
    """
    return type(pos) == dict and \
        'c' in pos and \
        'l' in pos and \
        type(pos['c']) == str and \
        type(pos['l']) == str and \
        pos['c'] in 'abc' and \
        pos['l'] in '123'


def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao X posicao -> booleano
    Devolve True apenas se os argumentos dados sao posicoes e
    sao iguais. Caso contrario, devolve False.
    """
    return eh_posicao(p1) and \
        eh_posicao(p2) and \
        obter_pos_c(p1) == obter_pos_c(p2) and \
        obter_pos_l(p1) == obter_pos_l(p2)


def posicao_para_str(pos):
    """
    posicao_para_str: posicao -> str
    Devolve a cadeira de caracteres 'cl' que representa a
    posicao dada.
    """
    return obter_pos_c(pos) + obter_pos_l(pos)


def obter_posicoes_adjacentes(pos):
    """
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    Devolve um tuplo com as posicoes adjacentes ah posicao dada,
    ordenado de acordo com a ordem de leitura do tabuleiro.
    """
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
