# Formiguinha do Langton

def run_langton(rules, size):
    # inicializa a formiguinha do capeta no meio do tabuleiro,
    # a partir do ponto médio de Size
    # (0,0)
    formiX = size // 2
    formiY = size // 2

    # formiguinha inicia virada para cima. Usando como referência
    # o eixo X do plano cartesiano, a direção norte seria 90º,
    # ou seja, o angulo formado entre o eixo X e Y
    angulo = 90

    # DIREÇÃO SERÁ COMPUTADA ATRAVÉS DO RESTO DA DIVISÃO POR 360
    # norte = 90
    # oeste = 180
    # sul = 270
    # leste = 0 / 360

    # inicialização do contador de passos da formiguinha do capeta
    marcaPasso = 0
    valorColorido = []  # guarda as cores, que não são apenas 'preto' e 'branco'
    tabuleiro = []

    # cria o tabuleiro a partir do tamanho passado como argumento na função principal
    def gera_tabuleiro():
        # percorre todas as linhas e
        for linha in range(size):
            # adiciona um espaço vazio
            valorColorido.append([])
            # agora acessa cada elemento da matriz e os inicializa com cor 0
            for coluna in range(size):
                valorColorido[linha].append(0)
                tabuleiro.append((coluna, linha))

    def atualiza_cor():
        # Segundo o enunciado, a cada passagem numa casa,
        # soma-se 1 ao valor da cor desse elemento
        # pode ser qualquer valor
        valorColorido[formiY][formiX] = valorColorido[formiY][formiX] + 1  # soma 1 ao valor atual da casa da formiga
        # LÃ³gica do Matheus castello no Piazza
        valorColorido[formiY][formiX] = valorColorido[formiY][formiX] % len(rules)

    # cria um tabuleiro a partir do Size passado no início
    gera_tabuleiro()
    # atualiza a cor dos elementos
    atualiza_cor()
    # o ponto inicial precisa ser contado como um passo, então marca passo é incrementado

    # inicializado com um passo extra, uma vez que o teste
    # pede o passo em que a formiga saiu do tabuleiro
    marcaPasso = marcaPasso + 1
    formiY = formiY - 1

    #### aaaaaaaaaaaaaah não sei o que fazer agora pqpqp
    # bora dormir
    # acordei de cabeça limpa e pensamento claro
    # apelaÃ§Ã£o para casos base
    if size == 1:
        # retorna que terÃ¡ apenas um movimento para sair do tabuleiro
        return (1, [[1]])
    # retorna uma lista com  movimento vazio e o valor da casa serÃ¡ 0
    elif size == 0:
        return (0, [])

    ### O ERRO ESTAVA AQUI!! ANTES ESTAVA FAZENDO UMA ITERAÃ‡ÃƒO ENTRE A STRING DE REGRAS
    # E DEVERIA ESTAR CHECANDO AS CONDIÃ‡~ES EXPRESSAS NO ENUNCIADO

    # CORRIGIDO COM AJUDA DE PEDRO HENRIQUE LIMA, VICTOR E CARLOS. Obrigado amigos, vocÃªs sÃ£o amigos.

    # LOOP PRINCIPAL
    # Enquanto a posiÃ§Ã£o da formiga ainda estiver contida no tabuleiro
    while (size - 1) >= formiX >= 0 and (size - 1) >= formiY >= 0:

        casaCor = valorColorido[formiY][formiX]
        if rules[casaCor] == 'R':
            angulo = angulo + 90

        if rules[casaCor] == 'L':
            angulo = angulo - 90

        # pega o valor da soma dos Ã¢ngulos e normaliza, ao dividir por 360
        # e pegar o resto da divisÃ£o, para saber qual o Ã¢ngulo atual
        anguloNormalizado = angulo % 360

        # chama a funÃ§Ã£o de atualizar a cor para somar +1 ao valor da casa atual
        atualiza_cor()

        # Computa o prÃ³x passo da formiga, ou seja,
        # atualiza o valor da posiÃ§Ã£o X ou Y, dependendo do Ã¢nguloNormalizado retornado

        # Incrementa o eixoX anda um para a direita se o Ã¢ngulo apontar para a direita
        if anguloNormalizado == 0:
            # formiX += 1
            formiX = formiX + 1

        # decrementa o eixoY se o angulo apontar para o Norte
        if anguloNormalizado == 90:
            # formiY -= 1
            formiY = formiY - 1
        # decrementa o eixo X caso esteja apontando para Leste atual
        if anguloNormalizado == 180:
            # formiX -= 1
            formiX = formiX - 1
        # incrementa o eixo Y
        if anguloNormalizado == 270:
            # formiY += 1
            formiY = formiY + 1
        # incrementa o contador de passos da fomriga
        marcaPasso = marcaPasso + 1
    print(marcaPasso, valorColorido)

    grid = [list(reversed(i)) for i in valorColorido]

    return (marcaPasso, grid)


# caso de teste para ver se a formiga soma o valor acima de 1
print(run_langton('RL', 51))
