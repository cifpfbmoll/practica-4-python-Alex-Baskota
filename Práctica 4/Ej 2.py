'''2) Pide al usuario 5 números y di si estos estaba en orden 
decreciente, creciente o desordenados.'''

num1=float(input("Introduzca el primer número: "))
num2=float(input("Introduzca el segundo número: "))
num3=float(input("Introduzca el tercer número: "))
num4=float(input("Introduzca el cuarto número: "))
num5=float(input("Introduzca el quinto número: "))

if num1<num2 and num2<num3 and num3<num4 and num4<num5:
    print("El orden de los números es ascendente.")
elif num1>num2 and num2>num3 and num3>num4 and num4>num5:
    print("El orden de los números es descendente")
else:
    print("Los números estan desordenados.")
