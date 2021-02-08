def run_length_encode_2d(array):
    
    #Quebrar matriz (list of lists )em um único array unidimensional
    novalista = []
    for sublista in array:
        for item in sublista:
            novalista.append(item)
    #return novalista
    anterior = novalista[0]
    contador = 0
    listaresultado = []

    for i in novalista:
        if i != anterior: 
            #if anterior:
            contaSequencia = (contador, anterior)
            listaresultado.append(contaSequencia)
            contador = 1
            anterior = i
        else:
            contador +=1
  
    else:
        try:
            contaSequencia = (contador, i)
            listaresultado.append(contaSequencia)
            return (listaresultado)
        except Exception as e:
            print("Exception encountered {e}".format(e=e)) 
            return (e, 1)
    return novalista


matriz = [[0, 0, 0],[2, 2, 1],[1, 1, 1]]
 
matriznova = [[1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 0, 0, 1],[1, 0, 1, 0, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1],[1, 0, 1, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 1, 1]]
 

print(run_length_encode_2d(matriznova))