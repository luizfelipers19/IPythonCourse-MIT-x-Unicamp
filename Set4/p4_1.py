

warehouse = {'a': 10, 'b': 20, 'c': 0}
print(warehouse)


def warehouse_process(dicionario, transacao):

    # confere se o produto em questão existe no dicionário, checando todas as chaves do dicionário e venrificando sua existência
    if transacao[1] in dicionario.keys():

        # realiza a soma dos respectivos produtos no dicionário do armazem
        if transacao[0] == 'receive':
            dicionario[(transacao[1])] = dicionario[(
                transacao[1])] + transacao[2]
            # return warehouse

        elif transacao[0] == 'ship':
            # Checa se o produto a ser retirado possui a quantidade necessária

            # Caso não possua o numero de itens necessários
            if (dicionario[(transacao[1])] - transacao[2]) < 0:
                # passa o valor 0 para a quantidade de produtos em estoque
                dicionario[transacao[1]] = 0
                # printa Not Enough, como pedido no enunciado
                print('not enough')

            # Caso a subtração dos itens por completo for possível, simplesmente subtrai a quantidade do armazém pela quantidade passada como argumento
            else:
                dicionario[(transacao[1])] = dicionario[(
                    transacao[1])] - transacao[2]
            # return warehouse

    # Caso o item não esteja no armazém, uma nova chave é criada a partir do índice passado como argumento e o valor é passado para essa chave
    else:

        dicionario[transacao[1]] = transacao[2]


# print de teste
print(warehouse_process(warehouse, ('receive', 'a', 39)))


class Warehouse:
    def __init__(self):
        self.dicionario = {}

    def process(self, transacao):

        # confere se o produto em questão existe no dicionário, checando todas as chaves do dicionário e venrificando sua existência
        if transacao[1] in self.dicionario.keys():

            # realiza a soma dos respectivos produtos no dicionário do armazem
            if transacao[0] == 'receive':
                self.dicionario[(transacao[1])] = self.dicionario[(
                    transacao[1])] + transacao[2]
                # return warehouse

            elif transacao[0] == 'ship':
                # Checa se o produto a ser retirado possui a quantidade necessária

                # Caso não possua o numero de itens necessários
                if (self.dicionario[(transacao[1])] - transacao[2]) < 0:
                    # passa o valor 0 para a quantidade de produtos em estoque
                    self.dicionario[transacao[1]] = 0
                    # printa Not Enough, como pedido no enunciado
                    print('not enough')

                # Caso a subtração dos itens por completo for possível, simplesmente subtrai a quantidade do armazém pela quantidade passada como argumento
                else:
                    self.dicionario[(transacao[1])] = self.dicionario[(
                        transacao[1])] - transacao[2]
                # return warehouse

        # Caso o item não esteja no armazém, uma nova chave é criada a partir do índice passado como argumento e o valor é passado para essa chave
        else:

            self.dicionario[transacao[1]] = transacao[2]

    def lookup(self, item):
        #confere se o elemento pesquisado por lookup existe no dicionário
        if item in self.dicionario.keys():
            #retorna o valor contido no armazem para determinado item
            return (self.dicionario[item])
        #retorna 0 caso não existir certo produto cadastrado no armazem
        else:
            return 0
