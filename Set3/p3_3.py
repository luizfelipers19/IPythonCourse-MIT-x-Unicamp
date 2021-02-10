#Mapeamento de dicionários
#função que mapeia todos os valores dos elementos do dicionário passado como argumento, e para cada elemento, executa a função também passada por argumento

def dictmap(d, f):
    for value in d:
        d[value] = f(d[value])
    return None
