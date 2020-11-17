#PRÁCTICA 4 --> EJERCICIO 4
# Pida al usuario tres números y un cuarto número, y compruebe
# si este último es divisor de los tres números primeros.

numero1 = int(input("Ponga un número: "))
numero2 = int(input("Ponga un número: "))
numero3 = int(input("Ponga un número: "))
numero4 = int(input("Ponga un número y le diré si es divisor de \n\
los anteriores: "))

if(numero1%numero4 == 0):
    print(numero4, "es divisor de", numero1)
if(numero2%numero4 == 0):
    print(numero4, "es divisor de", numero2)
if(numero3%numero4 == 0):
    print(numero4, "es divisor de", numero3)
if(numero1%numero4 != 0) and (numero2%numero4 != 0) and (numero3%numero4 != 0):
    print(numero4, "no es divisor de ninguno de los anteriores.")
