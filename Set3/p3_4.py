debt_dict = {'Joe': [5, 7], 'Denny': [20]}

print(debt_dict)

#João empresta muito dinheiro e pensa em contratar um agiota para matar os caloteiros,
# mas para isso, construiu um programa em Python para calcular as dívidas respectivas

#função que guarda a quantidade emprestada para cada pessoa
def lend_money(debts, person, amount):
    #se a pessoa estiver na lista de dívidas, soma a dívida ao seu montante de dívidas
    if person in debts.keys():
        debts[person].append(amount)
        #caso contrário, cria um item para a nova pessoa endividada e passa o valor da dívida para a variável criada
    else:
        debts[person] = [amount]
        
#função que calcula o quanto cada pessoa deve para João
def amount_owed_by(debts, person):
    #inicia com a dívida em 0 e percorre o array de pessoas
    devido = 0
    #caso a pessoa não esteja no array de dívidas, retorna 0, ou seja, não deve nada
    if person not in debts:
        return 0 #deve nada, nome limpo
    else:
        #caso a pessoa esteja no array de debitos, percorre todo os elementos de dívida dessa pessoa e soma até retornar o valor total da dívida de uma pessoa
        for i in range(0, len(debts[person])):
            devido += debts[person][i]
    return devido        

#Total devido para João. mlk tá voando
def total_amount_owed(debts):
    total_Devido = 0
    #percorre a lista de pessoas
    for person in debts.keys():
        for i in debts[person]:
            total_Devido += i
    return total_Devido


print(total_amount_owed(debt_dict))