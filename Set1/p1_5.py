size = 'small'
toppings =  ['presunto', 'abacaxi']
bacon = 'bacon'
anchovas = 'anchovas'
preco_base = 0
taxa = 0

if size == 'small':
    preco_base = 14

elif size == 'medium':
    preco_base = 16

elif size == 'large':
    preco_base = 18


for i in toppings:
    taxa = (12 + toppings.index(i) + len(i))/ 100
    preco_base = preco_base + (preco_base * taxa)
    print("Ate agora o preço é: ", preco_base)


print(preco_base)


for j in toppings:
    if j == 'bacon' or j=='anchovas':
        taxa_final = 0.1
        preco_final = preco_base + preco_base*taxa_final
    else:
        preco_final = preco_base

out = preco_final
print(out)