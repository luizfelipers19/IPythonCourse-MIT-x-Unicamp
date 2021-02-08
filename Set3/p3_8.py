def composite(f,g):
    return lambda x: f(g(x))

#print(composite)