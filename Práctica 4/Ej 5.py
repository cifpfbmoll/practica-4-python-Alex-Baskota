'''5) Pida al usuario un importe en euros y diga si el cajero automático le 
puede dar dicho importe utilizando el mismo billete y el más grande 
(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).'''
 	
importe = int(input("Introduzca un importe en euros: "))

if importe%500==0:
    billetes=importe/500
    print("El cajero devuelve" ,billetes, "de 500 euros")
elif(importe%200==0):
    billetes=importe/200
    print("El cajero devuelve" ,billetes, "de 200 euros")
elif(importe%100==0):
    billetes=importe/100
    print("El cajero devuelve" ,billetes, "de 100 euros")