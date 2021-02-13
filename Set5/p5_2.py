class Matrix:
    
    #Construtor da classe recebe uma matriz (listas aninhadas) e inicializa a matriz
    def __init__(self, matriz):
        self.matriz = matriz
    
    #Retorna o tamanho da matriz. Ex: (2x3), (3x3), etc...
    # Mas retorna numa tupla de formato (linhas, colunas)
    def size(self):
        
        #incializa contadores
        linhas = 0
        colunas = 0
        
        #itera sobre linhas e colunas e acumula a quantidade respectiva
        for linha in self.matriz:
            linhas +=1
        
        for coluna in self.matriz[0]:
            colunas +=1
            
        #salva os valores acumulados nas variáveis pedidas pelo exercício
        numrows = linhas
        numcols = colunas
        
        #retorna tupla contendo numRows e numCols
        print(numrows, numcols)
        return (numrows, numcols)
    
    #função que retorna o item passado via argumento
    def get(self, linha, coluna):
        #pega os argumentos e apenas acessa o valor correspondente do mapeamento,
        # retornando o valor do item escolhido no final
        valor = self.matriz[linha][coluna]
        print(valor)
        return valor
    
    #função da hora que altera o elemento especificado através do mapeamento de linhas e colunas,
    #e atualiza o valor desse elemento para o valor passado por referência
    def set(self, linha, coluna, valor):
        self.matriz[linha][coluna] = valor
        
    def row(self,linhaEscolhida):
        print(self.matriz[linhaEscolhida])
        return self.matriz[linhaEscolhida]
    
    def col(self, colunaEscolhida):
        #percorre tooooodas as linhas da matriz, e salva num array os elementos da colunaEscolhida (de cada linha) passada por argumento.
        #os elementos da colunaEscolhida de todas as linhas são salvos numa nova lista colunaEspecífica 
        colunaEspecifica = [self.matriz[linha][colunaEscolhida] for linha in range(len(self.matriz))]
        print(colunaEspecifica)
        return colunaEspecifica
        
    #matriz transposta -> [[1,2],[3,4]] = [[1,3],[2,4]]
    def transpose(self):
        #separa as linhas da matriz a partir do método zip, para iterar em cada linha
        separadas = zip(*self.matriz)
        #salva uma nova lista contendo os itens transpostos
        transposta = [list(linha) for linha in separadas]
        #retorna uma nova instância da classe Matrix,
        #com os novos valores computados em formato de matriz transposta
        transpostaFinal = Matrix(transposta)
        print(transpostaFinal)
        return transpostaFinal
    
    
    #Função para somar matrizes
    def add(self, other):
        #checagem do tipo da instância do outro objeto recebido por argumento
        
        #se other for do tipo Matrix:
        if isinstance(other, Matrix):
            
            #Se a Matrix em questão for do mesmo tamanho da matrix recebida (other)
            #### CHAMA A FUNÇÃO SIZE DEFINIDA NO INÍCIO DO PROBLEMA PARA COMPARAR
            #O TAMANHO E DIMENSÃO DAS MATRIZES SELF E OTHER
            if self.size() == other.size():
                #realiza adição de matrizes
                linhas = self.size()[0]
                colunas = self.size()[1]
                adicionada = Matrix(self.matriz)
                
                #percorre toda a matriz
                for linha in range(linhas):
                    for coluna in range(colunas):
                        #soma cada item da matriz original com os itens correspondente da matriz Other
                        adicionada.matriz[linha][coluna] += other.matriz[linha][coluna]
                return adicionada
            
            #caso os tamanhos checados de Self e Other sejam diferentes,
            # retorna nulo/None
            else:
                return None
            
        #caso o argumento Other seja um número único int ou float,
        # adiciona other a cada elemento da matriz
        elif isinstance(other, int) or isinstance(other, float):
            #cria uma variável nova para guardar o resultado da soma
            adcComum = Matrix(self.matriz)
            #percorre todos os elementos da matriz self em questão
            for linhas in range(self.size()[0]):
                for colunas in range(self.size()[1]):
                    #realiza a soma do valor de Other em tds os elementos da matriz original
                    adcComum.matriz[linhas][colunas] += other
            return adcComum
        
        else:
            return None
        
    #mudando a dunder function nativa do Python para funcionar apenas com matrizes
    def __add__(self, other):
        #chama a função add definida para somar duas matrizes ou 1 matriz e 1 número
        adicionado =  self.add(other)
        return adicionado
    
    
    #Copiei a função de add e substitui todos os operadores de adição por subtração
    def sub(self, other):
        #checagem do tipo da instância do outro objeto recebido por argumento
        
        #se other for do tipo Matrix:
        if isinstance(other, Matrix):
            
            #Se a Matrix em questão for do mesmo tamanho da matrix recebida (other)
            #### CHAMA A FUNÇÃO SIZE DEFINIDA NO INÍCIO DO PROBLEMA PARA COMPARAR
            #O TAMANHO E DIMENSÃO DAS MATRIZES SELF E OTHER
            if self.size() == other.size():
                #realiza adição de matrizes
                linhas = self.size()[0]
                colunas = self.size()[1]
                subtraida = Matrix(self.matriz)
                
                #percorre toda a matriz
                for linha in range(linhas):
                    for coluna in range(colunas):
                        #soma cada item da matriz original com os itens correspondente da matriz Other
                        subtraida.matriz[linha][coluna] -= other.matriz[linha][coluna]
                return subtraida
            
            #caso os tamanhos checados de Self e Other sejam diferentes,
            # retorna nulo/None
            else:
                return None
            
        #caso o argumento Other seja um número único int ou float,
        # subtrai other a cada elemento da matriz
        elif isinstance(other, int) or isinstance(other, float):
            #cria uma variável nova para guardar o resultado da soma
            subComum = Matrix(self.matriz)
            #percorre todos os elementos da matriz self em questão
            for linhas in range(self.size()[0]):
                for colunas in range(self.size()[1]):
                    #realiza a soma do valor de Other em tds os elementos da matriz original
                    subComum.matriz[linhas][colunas] -= other
            return subComum
        
        else:
            return None
        
    #mudando a dunder function nativa do Python para funcionar apenas com matrizes
    def __sub__(self, other):
        #chama a função add definida para somar duas matrizes ou 1 matriz e 1 número
        subtraido = self.sub(other)
        return subtraido
            
        
