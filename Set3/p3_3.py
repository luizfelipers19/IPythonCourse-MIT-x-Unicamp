def dictmap(d, f):
    for value in d:
        d[value] = f(d[value])
    return None
