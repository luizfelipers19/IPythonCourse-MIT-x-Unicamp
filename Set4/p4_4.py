#Operação em vetores
import math

class Vector:
    
    def __init__(self, lista):
        self.lista = lista
        
    def as_list(self):
        return self.lista
    
    def size(self):
        return len(self.lista)
