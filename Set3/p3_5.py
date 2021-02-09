# def approx_derivative(f, x, delta = 1e-6):
   
#     def a(x):
#         return f(x+delta)
#     def b(x):
#         return f(x-delta)
#     c = (a(x)-b(x))/(2*delta)
#     return c
    
# print( approx_derivative(lambda x : x + 2, 8.98))

# def approx_derivative_2(f, delta = 1e-6):
#     def g(x):
#             return ((f(x+delta))-(f(x-delta)))/(2*delta)
#     return g

# def approx_integral(f, lo, hi, num_regions):

#     span = list(range (1, num_regions + 1))

#     height = ((hi - lo)/num_regions)

#     def g(x):
#         return f(x)

#     comeco = g(lo)
    
#     for trap in span:
#         if trap == 1:
#             area = (g(lo)+ g(lo+height))*.5*height
#         elif trap == num_regions + 1 :
#             pass
#         else:
#             area = area + (g(lo+(trap-1)height)+ g(lo+(trap)*height)).5*height
        
#     return area

#print(approx_integral(lambda x : 2*x, 0, 4, 10))

def approx_derivative(f, x, delta = 1e-6):
   ##Definição de funções internas para calculo da aproximação da derivada
    def a(x):
        return f(x+delta)
    def b(x):
        return f(x-delta)
    c = (a(x)-b(x))/(2*delta)
    return c
    
print( approx_derivative(lambda x : x + 2, 8.98))

def approx_derivative_2(f, delta = 1e-6):
    def g(x):
            return ((f(x+delta))-(f(x-delta)))/(2*delta)
    return g

def approx_integral(f, lo, hi, num_regions):

    span = list(range (1, num_regions + 1))

    altura = ((hi - lo)/num_regions)

    def g(x):
        return f(x)

    comeco = g(lo)
    
    for trapezoidal in span:
        if trapezoidal == 1:
            area = (g(lo)+ g(lo+altura))*.5*altura
        elif trapezoidal == num_regions + 1 :
            pass
        else:
            area = area + (g(lo+(trapezoidal-1)*altura)+ g(lo+(trapezoidal)*altura))*.5*altura
        
    return area

print(approx_integral(lambda x : 2*x, 0, 4, 10))