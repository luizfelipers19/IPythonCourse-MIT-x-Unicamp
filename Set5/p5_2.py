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