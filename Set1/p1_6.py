#manter nome p_d , mas mudar o valor de p_d para outro numero impar
p_d = 11


#mudar nome
contido = 0
#mudar nome
total_grid = p_d **2

#importar biblioteca math para realizar os calculos com o valor de p_d
import math

#criação da  lista utilizando list comprehension
a = [[0] * p_d for i in range(p_d)]

#declaracao dos iteradores para laço de repetição
i = 0
j=0


for i in range(p_d):
#quebra de linha que não funciona
    print()
    for j in range(p_d):
        #preenche os valores dos elementos da lista A, com os valores das coordenadas (x,y) correspondente
        #divide o valor de pd na metade, para que haja uma metade negativa e outra positiva na matriz
            a[i][j] = ( math.ceil( i - p_d/2), math.ceil(j- p_d/2))
            # caso a distância calculada com o valor alocado de i e j satisfizerem a condição de serem menores que p_d/2
            if (math.ceil( i - p_d/2)**2 + math.ceil(j- p_d/2)**2)**0.5 < p_d/2:
                #soma 1 a variavel de contido
                contido+=1

print("Tenho pinto pequeno")

#Printa o numero de blocos contidos no círculo e o número de blocos totais
print(contido, total_grid)

#printa a razão entre os blocos contidos e os blocos totais
print(contido / total_grid)

#calculo da estimativa a partir da formula (Blocos_contidos / Blocos_totais) * 4
estimativa = (contido / total_grid)*4

#confirmação do resultado
print("Estimativa é: ", estimativa)

#variável Out, reconhecida pelo Gradescope recebe a estimativa
out = estimativa
#printa o valor final de Out
print(out)

#boapanois
