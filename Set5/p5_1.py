#Formiguinha do Langtão

def run_langton(rules, size):
    
    
    
    #inicializa a formiguinha do capeta no meio do tabuleiro,
    # a partir do ponto médio de Size
    #(0,0)
    formiX = size // 2
    formiY = size // 2
    
    #formiguinha inicia virada para cima. Usando como referência
    # o eixo X do plano cartesiano, a direção norte seria 90º, 
    # ou seja, o angulo formado entre o eixo X e Y
    angulo = 90
    
    #DIREÇÃO SERÁ COMPUTADA ATRAVÉS DO RESTO DA DIVISÃO POR 360
    #norte = 90
    #oeste = 180
    #sul = 270
    #leste = 0 / 360
    
    
    
    #inicialização do contador de passos da formiguinha do capeta
    marcaPasso = 0
    valorColorido = []  #guarda as cores, que não ão apenas 'preto' e 'branco'
    tabuleiro = []  
    
    #cria o tabuleiro a partir do tamanho passado como argumento na função principal
    def gera_tabuleiro():
        #percorre todas as linhas e
        for linha in range(size):
            #adiciona um espaço vazio 
            valorColorido.append([])
            #agora acessa cada elemento da matriz e os inicializa com cor 0 
            for coluna in range(size):
                valorColorido[linha].append(0)
                tabuleiro.append((coluna, linha))
                
    def atualiza_cor():
        #Segundo o enunciado, a cada passagem numa casa,
        # soma-se 1 ao valor da cor desse elemento
        # pode ser qualquer valor
        valorColorido[formiX][formiY] = valorColorido[formiX][formiY] + 1 #soma 1 ao valor atual da casa da formiga
        
        
        #Lógica do Matheus castello no Piazza
        valorColorido[formiX][formiY] = valorColorido[formiX][formiY] % len(rules) #
    
    
    #cria um tabuleiro a partir do Size passado no início    
    gera_tabuleiro()
    #atualiza a cor dos elementos
    atualiza_cor()
    #o ponto inicial precisa ser contado como um passo, então marca passo é incrementado
    marcaPasso = marcaPasso +1
    
    formiY = formiY -1
    
    #### aaaaaaaaaaaaaah não sei o que fazer agora pqpqp
    #bora dormir
    #acordei de cabeça limpa e pensamento claro
    #apelação para casos base
    if size == 1:
        #retorna que terá apenas um movimento para sair do tabuleiro
        return(1, [[1]])
    #retorna uma lista com  movimento vazio e o valor da casa será 0
    elif size == 0:
        return(0, [])
    
    #itera em todos os elementos da string Rules passada, para 
    letra = 0
    
    for letra in range(0, len(rules)):
        if rules[letra] == 'L':
            angulo = angulo - 90
            
        
        elif rules[letra] == 'R':
            angulo = angulo + 90
            
        #pega o valor da soma dos ângulos e normaliza, ao dividir por 360
        # e pegar o resto da divisão, para saber qual o ângulo atual
        anguloNormalizado = angulo % 360
        
        #chama a função de atualizar a cor para somar +1 ao valor da casa atual
        atualiza_cor()
    
        #Computa o próx passo da formiga, ou seja, 
        # atualiza o valor da posição X ou Y, dependendo do ânguloNormalizado retornado
        
        #Incrementa o eixoX anda um para a direita se o ângulo apontar para a direita
        if anguloNormalizado == 0:
            formiX = formiX + 1
        #decrementa o eixoY se o angulo apontar para o Norte
        if anguloNormalizado == 90:
            formiY = formiY -1
        #decrementa o eixo X caso esteja apontando para Leste atual
        if anguloNormalizado == 180:
            formiX = formiX -1
        #incrementa o eixo Y
        if anguloNormalizado == 270:
            formiY = formiY +1
            
        #incrementa o contador de passos da fomriga
        marcaPasso = marcaPasso +1
    
    print(marcaPasso, valorColorido)
    return(marcaPasso, valorColorido)
        
#caso de teste para ver se a formiga soma o valor acima de 1       
print(run_langton('LLRLLLLLLRLRLRR', 15))
    
    