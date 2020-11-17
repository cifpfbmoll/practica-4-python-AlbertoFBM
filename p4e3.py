# PRÁCTICA 4 --> EJERCICIO 3
# Pida al usuario si quiere calcular el área de un triángulo o un 
# cuadrado, y pida los datos según que caso y muestre el resultado.

print("Que área quiere calcular? La de un triángulo o un cuadrado?")

eleccion = input(" T/C? ")

if (eleccion == "T") or (eleccion == "t"):
    print("Ha elegido calcular la base de un triángulo.")
    base = float(input("Digame la base: "))
    altura = float(input("Digame la altura: "))
    area = (base * altura/2)
    print("El área de su triangulo es: ", area)
elif (eleccion == "C") or (eleccion == "c"):
    print("Ha elegido calcular la base de un cuadrado,")
    lado = float(input("Digame el valor de un lado: "))
    area = lado * lado
    print("El área de su cuadrado es: ", area)
else:
    print("Incorrecto, ponga T para el Triángulo o C para Cuadrado")