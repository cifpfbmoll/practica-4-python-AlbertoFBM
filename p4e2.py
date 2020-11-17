# PRÁCTICA 4 --> EJERCICIO 2
# Pida al usuario 5 números y diga si estos estaban en orden decreciente,
# creciente o desordenados.

print("ponga 5 numeros en orden creciente, decreciente o desordenados")
numero1 = int(input("Ponga el primer numero: "))
numero2 = int(input("Ponga el segundo numero: "))
numero3 = int(input("Ponga el tercer numero: "))
numero4 = int(input("Ponga el cuarto numero: "))
numero5 = int(input("Ponga el quinto numero: "))

if (numero1<numero2<numero3<numero4<numero5):
    print("El orden es creciente")
elif(numero1>numero2>numero3>numero4>numero5):
    print("el orden es decreciente")
else:
    print("Los números están desordenados")