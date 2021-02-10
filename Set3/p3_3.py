#Mapeamento de dicionários
#função que mapeia todos os valores dos elementos do dicionário passado como argumento, e para cada elemento, executa a função também passada por argumento
def dictmap(d, f):
    #percorre o dicionário d para substituir os valores
    for valor in d:
      #Os valores do dicionário são atualizados com o resultado da função definida para cada valor. A função é definida pelo Gradescope
        d[valor] = f(d[valor])
    #sem return, pois a função não deve possuir retorno
