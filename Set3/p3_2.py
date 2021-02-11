
#função recebe um dicionário, a primeira chave a ser trocada e a segunda chave a ser trocada. Ambas as chaves serão invertidas, mantendo os valores, apenas trocando as chaves de cada valor
def swap(d,k1,k2):
    #Inverte a ordem das chaves
    #aux = d[k1]
    #d[k2] = aux
    
    #inversão utlizando as belezas do Python
    d[k1], d[k2] = d[k2], d[k1]
    #A função retorna nada (Não usar NULL)
    return None

#dicionário de teste
dicionarioAurelio ={'cat': 'Katze', 'guinea pig': 'Meerschweinchen', 'dog': 'Hund'}
#chamada de teste
swap(dicionarioAurelio,'guinea pig','dog')
#conferir resultado
print(dicionarioAurelio)
