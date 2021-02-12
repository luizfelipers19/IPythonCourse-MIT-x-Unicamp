class Rational:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def maximoDivComum(self):
        nume = self.numerador
        denomi = self.denominador
        while denomi == True:
            nume, denomi = denomi, nume % denomi
        return nume
    
    #função para retornar o valor do numerador definido no construtor
    def get_numerator(self):
        valor = self.numerador
        int(valor)
        return valor    

    def get_denominator(self):
        valor = self.denominador
        int(valor)
        return valor
    
    def to_float(self):
        #retorna os valores de numerador e denominador
        # através das funções definidas na classe
        numera = self.get_numerator()
        denomina = self.get_denominator()
        razao = float(numera / denomina)
        return razao
    
    
        