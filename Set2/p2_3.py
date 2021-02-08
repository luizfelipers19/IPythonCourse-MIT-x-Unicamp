import numpy as np

def ndoors(n):

    abertas = []
    doors = [False] * n
    for i in range(n):
       for j in range(i, n, i+1):
           doors[j] = not doors[j]

       #print("Door %d:" % (i+1), 'open' if doors[i] else 'close')

    abertas = np.where(doors)[0]

    return abertas + 1

print(ndoors(100))