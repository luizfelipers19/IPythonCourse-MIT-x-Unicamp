#Operação em vetores
import math

class Vector:
    
    def __init__(self, lista):
        self.lista = lista
        
    def as_list(self):
        return self.lista
    
    def size(self):
        return len(self.lista)
#Magnitude do vetor (fórmula achada na net)
    def magnitude(self):
        totalMag = 0
        for counter in self.lista:
            totalMag += counter * counter
      
        return totalMag ** (.5)
    
    
    #CALCULA A
    #distancia euclidiana entre os elementos do vetor    
    def euclidean_distance(self, other):
        totalDist = 0
        for counter in range(len(self.lista)):
            totalDist = totalDist + (self.lista[counter] - other.as_list()[counter]) ** 2
        return totalDist ** (.5)
 
    #soma dois vetores muito doidos
    def __add__(self, other):
        #caso o outro argumento passado não seja um vetor,
        if isinstance(other, Vector) == False:
            return None
        #caso seja vetor, cria um novo vetor e percorre elemento por elemento, somando
        elif isinstance(other, Vector) == True:
            if len(self.lista) == len(other.lista):
                novoVetor = Vector(self.lista)
                for itens in range(len(other.lista)):
                    novoVetor.lista[itens] = self.lista[itens] + other.lista[itens]
                return novoVetor
        
        else:
            return None
        
