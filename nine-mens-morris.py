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
    if type(c) != str or type(l) != str or \
            len(c) != 1 or c not in 'abc' or \
            len(l) != 1 or l not in '123':
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
        len(pos['c']) == 1 and \
        pos['c'] in 'abc' and \
        len(pos['l']) == 1 and \
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


def posicao_em_lista(pos, l):
    """
    posicao_em_lista: posicao X iteravel -> booleano
    Devolve True se a posicao estiver no iteravel dado.
    Devolve False em caso contrário.
    """
    return any(posicoes_iguais(pos, x) for x in l)

############
# TAD Peca #
############


def cria_peca(peca):
    """
    cria_peca: str -> peca
    Recebe um identificador de jogador (ou peca livre) e
    devolve um dicionario que corresponde ah representacao
    interna da peca.
    R[peca] -> {'peca': peca}
    """
    if type(peca) != str or len(peca) != 1 or peca not in 'XO ':
        raise ValueError('cria_peca: argumento invalido')
    return {'peca': peca}


def cria_copia_peca(peca):
    """
    cria_copia_peca: peca -> peca
    Recebe uma peca e devolve uma copia nova da peca
    """
    return {'peca': peca['peca']}


def eh_peca(arg):
    """
    eh_peca: universal -> booleano
    Devolve True caso o seu argumento seja um TAD peca
    ou False em caso contrario.
    """
    return type(arg) == dict and \
        len(arg) == 1 and \
        'peca' in arg and \
        type(arg['peca']) == str and \
        len(arg['peca']) == 1 and \
        arg['peca'] in 'XO '


def pecas_iguais(p1, p2):
    """
    pecas_iguais: peca X peca -> booleano
    Devolve True apenas se os argumentos dados sao pecas e
    sao iguais. Caso contrario, devolve False.
    """
    return eh_peca(p1) and eh_peca(p2) and p1['peca'] == p2['peca']


def peca_para_str(peca):
    """
    peca_para_str: peca -> str
    Devolve a cadeira de caracteres que representa o jogador dono
    da peca.
    """
    return '[{}]'.format(peca['peca'])


def peca_para_inteiro(peca):
    """
    peca_para_inteiro: peca -> N
    Devolve um inteiro -1, 1 ou 0, de acordo com o jogador dono da peca.
    """
    return {'[X]': 1, '[O]': -1, '[ ]': 0}[peca_para_str(peca)]


def obter_peca_oponente(peca):
    """
    obter_peca_oponente: peca -> peca
    Devolve a peca correspondente ao oponente da peca dada.
    A peca vazia devolve uma peca vazia.
    """
    return cria_peca({0: ' ', 1: 'O', -1: 'X'}[peca_para_inteiro(peca)])

#################
# TAD Tabuleiro #
#################


def cria_tabuleiro():
    """
    cria_tabuleiro: {} -> tabuleiro
    Devolve um tabuleiro de jogo do moinho de 3x3 posicoes vazio

    """
    return {}


def cria_copia_tabuleiro(tabuleiro):
    """
    cria_copia_tabuleiro: tabuleiro -> tabuleiro
    Recebe um tabuleiro e devolve uma copia nova do tabuleiro
    """
    res = {}
    for pos in tabuleiro:
        res[pos] = cria_copia_peca(tabuleiro[pos])
    return res


def obter_peca(tabuleiro, pos):
    """
    obter_peca: tabuleiro X posicao -> peca
    Devolve a peca na posicao dada do tabuleiro.
    Se a posicao nao estiver ocupada, devolve uma peca livre
    """
    pos_str = posicao_para_str(pos)
    if pos_str not in tabuleiro:
        return cria_peca(' ')
    return tabuleiro[pos_str]


def obter_vetor(tabuleiro, s):
    """
    obter_vetor: tabuleiro X str -> tuplo de pecas
    Devolve todas as pecas da linha ou coluna especificada
    pelo seu argumento.
    """
    if s in 'abc':
        return tuple(obter_peca(tabuleiro, cria_posicao(s, l)) for l in '123')
    return tuple(obter_peca(tabuleiro, cria_posicao(c, s)) for c in 'abc')


def coloca_peca(tabuleiro, peca, pos):
    """
    coloca_peca: tabuleiro X peca X posicao -> tabuleiro
    Modifica destrutivamente o tabuleiro,
    colocando a peca dada na posicao dada.
    Devolve o proprio tabuleiro.
    """
    tabuleiro[posicao_para_str(pos)] = peca
    return tabuleiro


def remove_peca(tabuleiro, pos):
    """
    remove_peca: tabuleiro X posicao -> tabuleiro
    Modifica destrutivamente o tabuleiro, removendo a peca da posicao dada.
    Devolve o proprio tabuleiro.
    """
    del tabuleiro[posicao_para_str(pos)]
    return tabuleiro


def move_peca(tabuleiro, pos1, pos2):
    """
    move_peca: tabuleiro X posicao X posicao -> tabuleiro
    Modifica destrutivamente o tabuleiro, movendo a peca que se encontra
    na posicao 1 para a posicao 2.
    Devolve o proprio tabuleiro.
    """
    peca = obter_peca(tabuleiro, pos1)
    return remove_peca(coloca_peca(tabuleiro, peca, pos2), pos1)


def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal -> booleano
    Devolve True caso o seu argumento seja um TAD tabuleiro valido.
    Devolve False em caso contrario.
    """
    todas_pos = [c + l for c in 'abc' for l in '123']
    if type(arg) != dict or \
            len(arg) > 9 or \
            not all(map(lambda x: x in todas_pos, arg)) or \
            not all(map(lambda x: eh_peca(x), arg.values())):
        return False

    jogador1 = len(obter_posicoes_jogador(arg, cria_peca('X')))
    jogador2 = len(obter_posicoes_jogador(arg, cria_peca('O')))
    if jogador1 > 3 or jogador2 > 3 or abs(jogador1 - jogador2) > 1:
        return False

    ganhadores = set()
    for seccao in 'abc123':
        vetor = obter_vetor(arg, seccao)
        if pecas_iguais(vetor[0], vetor[1]) and \
                pecas_iguais(vetor[1], vetor[2]) and \
                not pecas_iguais(vetor[0], cria_peca(' ')):
            ganhadores.add(peca_para_inteiro(vetor[0]))
    return len(ganhadores) <= 1


def eh_posicao_livre(tabuleiro, pos):
    """
    eh_posicao_livre: tabuleiro X posicao -> booleano
    Devolve True caso a posicao dada no tabuleiro corresponda a uma
    peca livre.
    Devolve False em caso contrario.
    """
    return pecas_iguais(cria_peca(' '), obter_peca(tabuleiro, pos))


def tabuleiros_iguais(tabuleiro1, tabuleiro2):
    """
    tabuleiros_iguais: tabuleiro X tabuleiro -> booleano
    Devolve True se ambos os tabuleiros dados sao iguais.
    Devolve False em caso contrario.
    """
    todas_pos = [cria_posicao(c, l) for c in 'abc' for l in '123']
    return eh_tabuleiro(tabuleiro1) and \
        eh_tabuleiro(tabuleiro2) and \
        all(map(lambda pos:
                pecas_iguais(obter_peca(tabuleiro1, pos),
                             obter_peca(tabuleiro2, pos)),
                todas_pos))


def tabuleiro_para_str(tabuleiro):
    """
    tabuleiro_para_str: tabuleiro -> str
    Devolve a cadeira de caracteres que representa o tabuleiro.
    """
    todas_pos = [cria_posicao(c, l) for l in '123' for c in 'abc']
    return ("   a   b   c\n1 {}-{}-{}" +
            "\n   | \\ | / |\n2 {}-{}-{}" +
            "\n   | / | \\ |\n3 {}-{}-{}").format(
        *map(lambda x: peca_para_str(obter_peca(tabuleiro, x)), todas_pos)
    )


def tuplo_para_tabuleiro(t):
    """
    tuplo_para_tabuleiro: tuplo -> tabuleiro
    Devolve o tabuleiro que eh representado pelo tuplo dado,
    que por sim contem 3 tuplos, um para cada posicao.
    """
    todas_pos = [[cria_posicao(c, l) for c in 'abc'] for l in '123']
    tab = cria_tabuleiro()
    for i in range(3):
        for j in range(3):
            peca = {-1: 'O', 0: ' ', 1: 'X'}[t[i][j]]
            coloca_peca(tab, cria_peca(peca), todas_pos[i][j])
    return tab


def obter_ganhador(tabuleiro):
    """
    obter_ganhador: tabuleiro -> peca
    Devolve uma peca do jogador que tenha as suas 3 pecas
    em tinha na vertical ou na horizontal no tabuleiro.
    """
    for seccao in 'abc123':
        vetor = obter_vetor(tabuleiro, seccao)
        if pecas_iguais(vetor[0], vetor[1]) and \
                pecas_iguais(vetor[1], vetor[2]) and \
                not pecas_iguais(vetor[0], cria_peca(' ')):
            return vetor[0]
    return cria_peca(' ')


def obter_posicoes_livres(tabuleiro):
    """
    obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    Devolve um tuplo com as posicoes nao ocupadas pelas pecas de
    qualquer um dos dois jogadores na ordem de leitura do tabuleiro.
    """
    return obter_posicoes_jogador(tabuleiro, cria_peca(' '))


def obter_posicoes_jogador(tabuleiro, peca):
    """
    obter_posicoes_livres: tabuleiro X peca -> tuplo de posicoes
    Devolve um tuplo com as posicoes ocupadas pelas pecas do jogador
    dado na ordem de leitura do tabuleiro.
    """
    todas_pos = [cria_posicao(c, l) for l in '123' for c in 'abc']
    return tuple(pos
                 for pos in todas_pos
                 if pecas_iguais(peca, obter_peca(tabuleiro, pos)))

######################
# Funcoes adicionais #
######################


def obter_movimento_manual(tabuleiro, peca):
    """
    obter_movimento_manual: tabuleiro X peca -> tuplo de posicoes
    Recebe um tabuleiro e uma peca de jogador, devolve um tuplo com
    uma ou duas posicoes, que representam uma posicao ou um movimento,
    introduzido pelo jogador.
    """
    eh_movimento = len(obter_posicoes_livres(tabuleiro)) <= 3

    if eh_movimento:
        mov = input("Turno do jogador. Escolha um movimento: ")
        if len(mov) == 4:
            pos_de, pos_para = cria_posicao(mov[0], mov[1]), \
                cria_posicao(mov[2], mov[3])
            if pecas_iguais(peca, obter_peca(tabuleiro, pos_de)) and \
                (posicoes_iguais(pos_de, pos_para) or
                 (pecas_iguais(cria_peca(' '),
                               obter_peca(tabuleiro, pos_para)) and
                    posicao_em_lista(pos_para,
                                     obter_posicoes_adjacentes(pos_de)))):
                return (pos_de, pos_para)
    else:
        pos = input("Turno do jogador. Escolha uma posicao: ")
        if len(pos) == 2:
            pos = cria_posicao(pos[0], pos[1])
            if pecas_iguais(cria_peca(' '), obter_peca(tabuleiro, pos)):
                return (pos, )

    raise ValueError("obter_movimento_manual: escolha invalida")


def crit_vitoria(tabuleiro, peca):
    """
    crit_vitoria: tabuleiro X peca -> posicao
    Verifica o criterio vitoria ou bloqueio para a fase de colocacao.
    Retorna a posicao a jogar, ou None se o criterio nao se verificar.
    """
    for pos in obter_posicoes_livres(tabuleiro):
        copia_tab = cria_copia_tabuleiro(tabuleiro)
        ganhador = obter_ganhador(coloca_peca(copia_tab, peca, pos))
        if pecas_iguais(peca, ganhador):
            return pos


def crit_posicoes(tabuleiro, posicoes):
    """
    crit_posicoes: tabuleiro X tuplo de posicoes -> posicao
    Devolve a primeira posicao, do tuplo de posicoes, que se encontra
    livre no tabuleiro dado.
    """
    cantos = [cria_posicao(x[0], x[1]) for x in posicoes]
    livres = obter_posicoes_livres(tabuleiro)
    for canto in cantos:
        if posicao_em_lista(canto, livres):
            return canto


def obter_movimento_facil(tabuleiro, peca):
    """
    obter_movimento_facil: tabuleiro X peca -> tuplo de posicoes
    Recebe um tabuleiro e uma peca, e devolve um tuplo de duas posicoes
    correspondente ao movimento que o jogador deve efetuar na dificuldade facil
    """
    for pos in obter_posicoes_jogador(tabuleiro, peca):
        for pos_adj in obter_posicoes_adjacentes(pos):
            if pecas_iguais(cria_peca(' '), obter_peca(tabuleiro, pos_adj)):
                return (pos, pos_adj)
    return (obter_posicoes_jogador(tabuleiro, peca)[0], ) * 2


def minimax(tabuleiro, jogador, profundidade, seq_movimentos):
    """
    minimax: tabuleiro X jogador X N X tuplo de tuplos de posicoes ->
    tuplo de posicoes X tuplo de tuplo de posicoes
    """
    ganhador = obter_ganhador(tabuleiro)
    if not pecas_iguais(cria_peca(' '), ganhador) or profundidade == 0:
        return peca_para_inteiro(ganhador), seq_movimentos

    melhor_res, melhor_seq_mov = -peca_para_inteiro(jogador), ()
    posicoes_livres = obter_posicoes_livres(tabuleiro)
    for pos in obter_posicoes_jogador(tabuleiro, jogador):
        for pos_adj in obter_posicoes_adjacentes(pos):
            if posicao_em_lista(pos_adj, posicoes_livres):
                copia_tabuleiro = cria_copia_tabuleiro(tabuleiro)
                move_peca(copia_tabuleiro, pos, pos_adj)
                novo_res, nova_seq_mov = \
                    minimax(copia_tabuleiro, obter_peca_oponente(jogador),
                            profundidade - 1, seq_movimentos + (pos, pos_adj))
                peca_int = peca_para_inteiro(jogador)
                if melhor_seq_mov == () or \
                    (peca_int == 1 and novo_res > melhor_res) or \
                        (peca_int == -1 and novo_res < melhor_res):
                    melhor_res, melhor_seq_mov = \
                        novo_res, nova_seq_mov
    if melhor_seq_mov == ():
        melhor_seq_mov = (obter_posicoes_jogador(tabuleiro, jogador)[0], ) * 2
    return melhor_res, melhor_seq_mov


def obter_movimento_auto(tabuleiro, peca, dificuldade):
    """
    obter_movimento_auto: tabuleiro X peca X str -> tuplo de posicoes
    Recebe um tabuleiro, uma peca e a dificuldade do jogo, e devolve um tuplo
    com uma ou duas posicoes, que representam uma posicao ou movimento
    escolhido automaticamente.
    """

    eh_movimento = len(obter_posicoes_livres(tabuleiro)) <= 3
    if not eh_movimento:
        criterios = (
            lambda: crit_vitoria(tabuleiro, peca),
            lambda: crit_vitoria(tabuleiro, obter_peca_oponente(peca)),
            lambda: crit_posicoes(tabuleiro, ('b2', )),
            lambda: crit_posicoes(tabuleiro, ('a1', 'c1', 'a3', 'c3')),
            lambda: crit_posicoes(tabuleiro, ('b1', 'a2', 'c2', 'b3'))
        )
        for criterio in criterios:
            pos = criterio()
            if pos:
                return (pos, )

    if dificuldade == 'facil':
        return obter_movimento_facil(tabuleiro, peca)

    if dificuldade == 'normal':
        return minimax(tabuleiro, peca, 1, ())[1][:2]

    if dificuldade == 'dificil':
        return minimax(tabuleiro, peca, 5, ())[1][:2]
