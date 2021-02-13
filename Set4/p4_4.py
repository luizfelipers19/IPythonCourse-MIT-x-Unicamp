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
        def __truediv__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0 or other == 0.0:
                return None
            else:
                res = Vector(self.lista)
                
                for itens in range(len(self.lista)):
                    res.lista[itens] = res.lista[itens] / other
                return res
        
        else:
            return None
        
        
    def __mul__(self,other):
        
        if type(other) == int or type(other) == float:
            res = Vector(self.lista)
        
            for itens in range(len(self.lista)):
                res.lista[itens] = res.lista[itens] * other
            return res
        
        elif type(other) == Vector:
        
            if self.size() == other.size():
                resp = 0
                
                aux = Vector(self.lista)
                
                for itens in range(self.size()):
                    resp = resp + self.lista[itens] * other.lista[itens]
                return resp
            
            elif self.size != other.size:
                return None
            
        elif type(other) != Vector or type(other) != int or type(other) != float:
            return None
        
        
        else:
            return None

    def __sub__(self,other):
        if type(other) != Vector:
            return None
            
        elif len(self.lista) == len(other.lista):

            subt = Vector(self.lista)

            for itens in range(len(other.lista)):
                subt.lista[itens] = self.lista[itens] - other.lista[itens]

            return subt

        else:
            return None
        
        ##Não precisa de other, pois usa o vetor original
    def normalized(self):
        #cria um novo vetor e atribui a variável normal
        normalizada = Vector(self.lista)
        mag = self.magnitude()
        
        #percorre todos os elementos da lista
        # e divide os valores pela magnitude,
        # devolvendo o valor normalizado
        for itens in range(len(self.lista)):
            normalizada.lista[itens] = (self.lista[itens]/mag)
        return normalizada
        
