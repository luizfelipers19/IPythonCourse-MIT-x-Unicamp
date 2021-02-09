def hailstone_sequence(a_0):
    lista = [a_0]
    while a_0 != 1:
        if (a_0 %2) == 0:
            a_0 = a_0 //2
            lista.append(a_0)
        else:
            a_0 = (a_0 * 3) + 1
            lista.append(a_0)
    return lista

print(hailstone_sequence(3))