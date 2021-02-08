import string

def caesar_cipher(fraseEntrada, deslocamento):
    abecedario = string.ascii_lowercase
    chars = string.digits
    #inicialização da variável temporária que guardará o valor das frases novas (vazias)
    refactored_sentence = ''
    
    fraseNova = ''
    fraseEntrada = fraseEntrada.lower()
    
    #percorre todos os caracteres da frase de entrada
    for i in fraseEntrada:
        indice = abecedario.find(i)
        
        
        
        if indice == -1:
            refactored_sentence = refactored_sentence + i
        
        else:
            indiceAtualizado = indice + deslocamento
            indice - deslocamento
            indiceAtualizado = indiceAtualizado % len(abecedario)
            refactored_sentence += abecedario[indiceAtualizado : indiceAtualizado + 1]


    #atualiza~]ao final da frase
    for x in refactored_sentence:
        indiceCripto = chars.find(x)
        if indiceCripto == -1:
            fraseNova = fraseNova + x
        else:
            indiceAtualizado = indiceCripto + deslocamento
            indiceCripto - deslocamento
            indiceAtualizado = indiceAtualizado % len(chars)
            fraseNova = fraseNova + chars[indiceAtualizado : indiceAtualizado + 1]

#retorna frase encriptada
    return fraseNova


#Conjunto de testes contido no exemplo
print(caesar_cipher("hot dogs are 5.00 here?!?",2))

print(caesar_cipher("don't you feel like a roman emperor?",13))

print(caesar_cipher("Delegado Da Cunha prende traficante no Estado de São Paulo", 2))