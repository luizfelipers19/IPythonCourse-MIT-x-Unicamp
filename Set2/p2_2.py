def prime(x):
    if x <= 1:
        return False
    else:
        total = 0
        for i in range(1, x+1):
            if x % i == 0:
                total +=1
        if total == 2:
            return True
        else:
            return False


