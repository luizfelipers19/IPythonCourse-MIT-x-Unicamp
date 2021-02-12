class Rational:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def maximoDivComum(self):
        #Algoritimo Euclideano
        nume = self.numerador
        denomi = self.denominador
        #enquanto o denominador for maior que o numerador
        while denomi:
            #inverte numerador e denominador, e retorna para o numerador,
            # o resto da divisão entre numerador e denominador
            nume, denomi = denomi, nume % denomi
        return nume
    
    #função para retornar o valor do numerador definido no construtor
    def get_numerator(self):
        valor = self.numerador
        int(valor)
        print(valor)
        return valor    

    def get_denominator(self):
        valor = self.denominador
        int(valor)
        print(valor)
        return valor
    
    def to_float(self):
        #retorna os valores de numerador e denominador
        # através das funções definidas na classe
        numera = self.get_numerator()
        denomina = self.get_denominator()
        razao = float(numera / denomina)
        print(razao)
        return razao
    
    
    #Retorna o reciproco, a partir da dúvida tirada em aula do dia 11/02
    #Reciproco é o inverso
    def reciprocal(self):
        #Para uma fração, o número recíproco é somente uma fração diferente,
        # com os números “trocados”, o de cima pelo de baixo. 
        # Por exemplo, o recíproco de 3/4 é 4/3.
        print(Rational(self.get_denominator(), self.get_numerator()))
        return Rational(self.get_denominator(), self.get_numerator())
    
    def reduce(self):
        #Reduz a fração o máximo possível, a partir do máximo divisor comum encontrado
        mdc = self.maximoDivComum()
        #retorna um numero de classe Rational, a partir da divisão do numerador e denominador pelo MDC encontrado
        reduzidaAoMaximo = Rational(int(self.numerador / mdc), int(self.denominador / mdc))
        print(reduzidaAoMaximo)
        return reduzidaAoMaximo
