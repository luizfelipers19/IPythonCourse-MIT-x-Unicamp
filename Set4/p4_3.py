class Rational:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # função para retornar o valor do numerador definido no construtor

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
        # retorna os valores de numerador e denominador
        # através das funções definidas na classe
        numera = self.get_numerator()
        denomina = self.get_denominator()
        razao = float(numera / denomina)
        print(razao)
        return razao

    def maximoDivComum(self):
        # Algoritimo Euclideano
        nume = self.numerador
        denomi = self.denominador
        # enquanto o denominador for maior que o numerador
        while denomi:
            # inverte numerador e denominador, e retorna para o numerador,
            # o resto da divisão entre numerador e denominador
            nume, denomi = denomi, nume % denomi
        return nume

    # Retorna o reciproco, a partir da dúvida tirada em aula do dia 11/02
    # Reciproco é o inverso
    def reciprocal(self):
        # Para uma fração, o número recíproco é somente uma fração diferente,
        # com os números “trocados”, o de cima pelo de baixo.
        # Por exemplo, o recíproco de 3/4 é 4/3.
        print(Rational(self.get_denominator(), self.get_numerator()))
        return Rational(self.get_denominator(), self.get_numerator())

    def reduce(self):
        # Reduz a fração o máximo possível, a partir do máximo divisor comum encontrado
        mdc = self.maximoDivComum()
        # retorna um numero de classe Rational, a partir da divisão do numerador e denominador pelo MDC encontrado
        reduzidaAoMaximo = Rational(
            int(self.numerador / mdc), int(self.denominador / mdc))
        print(reduzidaAoMaximo)
        return reduzidaAoMaximo

#Função que realiza a soma 
    def __add__(self, other):
        #Se o tipo do objeto passado por argumento for int
        if isinstance(other, int):
            #realiza a soma de frações, igualando os denominadores e multiplicando na proporção certa os numeradores
            val = Rational(self.numerador+self.denominador * other, self.denominador)
            return val.reduce()
        elif isinstance(other, Rational):
            #equilibra as frações e realiza a soma
            val = Rational(self.numerador*other.get_denominator()+other.get_numerator()*self.denominador, self.denominador*other.get_denominator())
            return val.reduce()
        #Transforma em float e soma a porra toda
        elif isinstance(other, float):
            val = (self.to_float() + other)
            return val
        
        #Caso não seja int, Rational e nem float, retorna um valor nulo
        else:
            return None
        
        #retorna a multiplicação de Self e Other
    def __mul__(self,other):
        #multiplica o numerador da original com a outra fração e mantém o denominador
        if isinstance(other, int):
            return Rational(self.numerador * other, self.denominador)
        #multiplica as frações, mas pega os valores a partir das funções definidas get_numerator e get.denominator
        elif isinstance(other, Rational):
            return Rational(self.numerador * other.get_numerator(), self.denominador*other.get_denominator())
        
        elif isinstance(other,float):
            return self.to_float()* other
        
        else:
            return None
		
  
#   #Mesma bosta da função de adicionar, só trocar o operador para subtração
#     def __sub__(self, other):
#         if isinstance(other, int):
#             return Rational(self.numerador - self.denominador * other, self.denominador)
#         elif isinstance(other, Rational):
#             return Rational(self.numerador * other.get_denominator() - other.get_numerator()*self.denominador, self.denominador*other.get_denominator())
#         elif isinstance(other, float):
#             return self.to_float() - other
#         else:
#             return None


#Copiei e colei a função de somar e mudei apenas o nome pq a estrutura é a msm coisa, só muda o operador
    def __sub__(self, other):
        #Se o tipo do objeto passado por argumento for int
        if isinstance(other, int):
            #realiza a soma de frações, igualando os denominadores e multiplicando na proporção certa os numeradores
            val = Rational(self.numerador-self.denominador * other, self.denominador)
            return val.reduce()
        elif isinstance(other, Rational):
            #equilibra as frações e realiza a soma
            val = Rational(self.numerador*other.get_denominator()-other.get_numerator()*self.denominador, self.denominador*other.get_denominator())
            return val.reduce()
        #Transforma em float e soma a porra toda
        elif isinstance(other, float):
            val = (self.to_float() - other)
            return val
        
        #Caso não seja int, Rational e nem float, retorna um valor nulo
        else:
            return None
        
        
        

    #na divisão de frações, deve-se multiplicar a primeira fração pelo inverso da segunda
    def __truediv__(self, other):
        if isinstance(other, int):
             #realiza a divisão de frações, igualando os denominadores e multiplicando na proporção certa os numeradores
            val = Rational(self.numerador, self.denominador * other)
            return val.reduce()
        elif isinstance(other,Rational):
            val= self.__mul__(other.reciprocal())
            return val.reduce()
        elif isinstance(other,float):
            val = self.to_float()/other
            return val
        else:
            return None
        
    


