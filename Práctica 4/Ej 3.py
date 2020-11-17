'''3)Pide al usuario si quiere calcular el área de un triángulo o un
cuadrado, y los datos según que caso y muestra el resultado.'''

figura = input("De qué figura quiere calcular el área: triángulo o cuadrado? ")
cuadrado = str("cuadrado")
triangulo = str("triángulo")



if (figura==cuadrado):
    lado_cuadrado = float(input("Introduzca el lado del cuadrado: "))
    area_cuadrado = lado_cuadrado ** 2
    print(lado_cuadrado)
    print(area_cuadrado)
elif (figura==triangulo):
    base_triangulo = float(input("Introduzca la base del triángulo: "))
    altura_triangulo = float(input("Introduzca la altura del triángulo "))
    area_triangulo = (base_triangulo * altura_triangulo) / 2
    
    print(area_triangulo)

#por qué no me imprime area_triangulo y area_cuadrado

