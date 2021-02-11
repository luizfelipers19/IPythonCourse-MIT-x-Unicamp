
##Código adaptado de estrutura de dados, onde percorre uma estrutura de árvore e compara os elementos

def binary_tree_max(tree):
    #guarda a variável max, passando o valor do nó inicial
    valorMaximo = tree["value"]
    #percorre todos os nós filhos do nó (iteratividade)
    for child in tree["children"]:
        #caso o valor atual seja maior do que o valor salvo em valorMaximo, esse valor é salvo em valorMaximo
        if valorMaximo < tree_max(child):
            valorMaximo = tree_max(child) #salva valorMaximo
    return valorMaximo #retorna o valor máximo encontrado

def tree_max(tree):
    #guarda a variável max, passando o valor do nó inicial
    valorMaximo = tree["value"]
    #percorre todos os nós filhos do nó (iteratividade)
    for child in tree["children"]:
        #caso o valor atual seja maior do que o valor salvo em valorMaximo, esse valor é salvo em valorMaximo
        if valorMaximo < tree_max(child):
            valorMaximo = tree_max(child) #salva valorMaximo
    return valorMaximo #retorna o valor máximo encontrado

#arvore do conjunto de testes do exercício
arvora = {'value': 13, 
 'children': [{'value': 7, 'children': []},
              {'value': 8,
               'children': [{'value': 99, 'children': []},
                            {'value': 16,
                             'children': [{'value': 77, 'children': []}]},
                            {'value': 42, 'children': []}]}]}

#printa o resultado para teste
print(tree_max(arvora))