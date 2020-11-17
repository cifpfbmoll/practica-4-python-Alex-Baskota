'''1) Realiza un programa que pida al usuario 5 números y diga 
cuál es el mayor y cuál el menor.'''

num1=float(input("Introduzca el primer número: "))
num2=float(input("Introduzca el segundo número: "))
num3=float(input("Introduzca el tercer número: "))
num4=float(input("Introduzca el cuarto número: "))
num5=float(input("Introduzca el quinto número: "))


#1) Si el número es el +grande, habría un nuevo mayor.
#2) Si no es el +grande, podría ser el +pequeño.
#3) Si es el +pequeño, habría un nuevo menor.
#4) Si ninguno es el +grande o el +pequeño, se mantendrian los valores anteriores.

'''else = cualquier otra condición
elif = otra condición específica 

Ambos actúan solamente cuando no se cumple la condición if, es decir,
si se cumple if, el programa no tendrá en cuenta else y elif.'''


menor=mayor=num1
if num2>mayor:
    mayor=num2
else:
    if num2<menor:
        menor=num2

if num3>mayor:
    mayor=num3
else:
    if num3<menor:
        menor=num3

if num4>mayor:
    mayor=num4
else:
    if num4<menor:
        menor=num4

if num5>mayor:
    mayor=num5
else:
    if num5<menor:
        menor=num5

print(mayor,"es el mayor y",menor,"es el menor.")