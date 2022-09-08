#Quiz: determinar si un numero de 5 cifras es capicua.

import math
s=""

print("----------------------")
print("----NUMERO-CAPICUA----")
print("----------------------")

#INPUT
n=int(input("Digite un numero de cinco cifras: "))

if 10000> n or n > 99999:
    print("Error! El numero ingresado no es de cinco cifras.")


#PROCESAMIENTO
c5=int(n/10000)
c4=int((n-(c5*10000)) /1000) 
c3=int((n-((c5*10000)+(c4*1000))) /100) 
c2=int((n-((c5*10000)+(c4*1000)+(c3*100))) / 10)
c1=n - ((c5 * 10000) + (c4 * 1000) + (c3 * 100) + (c2 * 10))
f=int(str(c1)+str(c2)+str(c3)+str(c4)+str(c5))

if n == f:
        print("Si es un numero capicua") 
else: 
        print("No es un numero capicua")

