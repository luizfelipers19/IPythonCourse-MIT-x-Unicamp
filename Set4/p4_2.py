import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)
    
    
class Triangle:
    
    #construtor do triangulo a partir dos pontos
    def __init__(self, ponto1, ponto2, ponto3):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        
        
    def compara_floats(x,y):
        #retorna a diferença do valor absoluto entre dois floats e compara se é a diferença é menor que 10^-6,
        # ou seja, se a diferença for uma diferença insignificante (de exponente -6), são considerados praticamente iguais
        if abs(x-y) <= 10**(-6):
            return True
        else:
            return False


    def side_lengths(self):
        #calcula o comprimento de cada lado a partir do calculo da distância entre pontos => Distância Euclidiana (Definição na classe Point)
        
        #ponto1 -> ponto2    / A -> B
        dist1 = self.ponto1.euclidean_distance(self.ponto2)
        #ponto2 -> ponto3   / B -> C
        dist2 = self.ponto2.euclidean_distance(self.ponto3)
        #ponto3 -> ponto1    / C -> A
        dist3 = self.ponto3.euclidean_distance(self.ponto1)
        
        distancias = (dist1,dist2, dist3)
        
        return distancias
    
    def angles(self):
        a1 = self.angle_between(ponto1, ponto2)
        a2 = self.angle_between(ponto2, ponto3)
        a3 = self.angle_between(ponto3, ponto1)
        
        angulos = (a1, a2, a3)
        
        return angulos
        
        
    def side_classification(self):
        lado1 = self.side_lengths()[0]
        lado2 = self.side_lengths()[1]
        lado3 = self.side_lengths()[2]

        #se todos os lados forem iguais, é equilatero
        
        
            #caso isosceles -> dois lados iguais e um lado diferente -> checa todos os casos
        if(compara_floats(lado1,lado2) == True and compara_floats(lado1, lado3) == False) or (compara_floats(lado2,lado3) == True and compara_floats(lado1, lado2) == False) or (compara_floats(lado3,lado1) == True and compara_floats(lado2, lado3) == False):
            print("isosceles")
            return 'isosceles'
        
        #se todos os lados forem iguais, é equilátero
        #lado1 == lado2 == lado3
        
        elif (compara_floats(lado1,lado2) and compara_floats(lado2, lado3) and compara_floats(lado3, lado1)):
        
            print("equilateral")
            return 'equilateral'
        
        
        #nem lembro o que é o escaleno, mas é o que sobrou   
        else:
            print("scalene")
            return 'scalene'
        
        
        
    
    def perimeter(self):
        lado1 = self.side_lengths()[0]
        lado2 = self.side_lengths()[1]
        lado3 = self.side_lengths()[2]
        
        perimetro = lado1 + lado2 + lado3
        print(perimetro)
        return perimetro