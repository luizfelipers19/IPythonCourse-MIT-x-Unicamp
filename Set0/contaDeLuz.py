kwh_used = 500

gasto = abs(kwh_used)

if(gasto <= 500):
    conta = gasto * 0.45

elif(gasto > 500 and gasto <=1500):
    conta = (500*0.45)+((gasto - 500)* 0.74)

elif(gasto > 1500 and gasto <= 2500):
    conta = (500*0.45)+((1500 - 500)* 0.74)+ ((gasto - 1500)*1.2)
elif(gasto > 2500):
    conta = (500*0.45)+((1500 - 500)* 0.74)+ ((2500 - 1500)*1.2) + ((gasto - 2500)* 2)

contafinal = conta * 1.2

out = contafinal
print(out)
