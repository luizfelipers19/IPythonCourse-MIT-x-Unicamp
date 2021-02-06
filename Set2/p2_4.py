def largest_number(input_list):
    best_so_far = -9999999999999999999999999999999

    if len(input_list) <= 1:
        return None

    for i in input_list:
        if i > best_so_far:
            best_so_far = i
    return best_so_far

def second_largest_number(lista):
    if len(lista) <= 1:
        return None
    else:
        lista.sort()
        return lista[-2]

#x = [1,2,3,5,85,7,6,9, 111, 99, 56, 250, 35]
#print("O maior número contido nessa merda é o: ", largest_number(x))

print(second_largest_number([]))
print(second_largest_number([2]))
print(second_largest_number([94, 87, 20, 35]))
print(second_largest_number([1, 2, 3, 3, 3]))
print(second_largest_number([20, -1, -10]))
