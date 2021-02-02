a=1
b=2
c=3

delta = b**2 - 4*(a*c)
print(delta)


    

x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

out = x1,x2
print(out)
