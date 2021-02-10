
#Mapeamento de dicionários
#função que mapeia todos os valores dos elementos do dicionário passado como argumento, e para cada elemento, executa a função também passada por argumento
def dictmap(d, f):
    #percorre o dicionário d para substituir os valores
    for valor in d:
      #Os valores do dicionário são atualizados com o resultado da função definida para cada valor. A função é definida pelo Gradescope
        d[valor] = f(d[valor])
    #sem return, pois a função não retorna nada

#definição de função besta para teste. Dobra o valor passado como argumento
def dobra_Valor(n):
    return n*2

#teste de função besta com valor passado = 2. Valor esperado = 4
print(dobra_Valor(2))
#definição de dicionario de testes: 1,2,3,4, 5 mil, o Vinicius é tão esperto que já fugiu do Brasil
dic = { 'um':1, 'dois':2, 'tres':3, 'quatro': 4, 'cinco_mil':5000 }

#printa o dicionário de testes em sua forma original
print(dic)
#executa a função dictmap no dicionário de testes. Como não retorna nada, os valores são apenas atualizados
dictmap(dic, dobra_Valor)

#printa o dicionário de testes em sua forma atualizada
print(dic)
