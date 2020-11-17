# PRÁCTICA 4 --> EJERCICIO 1
# Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.

print("Ponga 5 números y te diré cuál es al mayor y cuál es el menor")

numero1 = int(input("Ponga el primer numero: "))
numero2 = int(input("Ponga el segundo numero: "))
numero3 = int(input("Ponga el tercer numero: "))
numero4 = int(input("Ponga el cuarto numero: "))
numero5 = int(input("Ponga el quinto numero: "))

if(numero1>numero2) and (numero1>numero3) and (numero1>numero4) and (numero1>numero5):
    print("El número mayor es", numero1)
elif(numero2>numero1) and (numero2>numero3) and (numero2>numero4) and (numero2>numero5):
    print("El número mayor es", numero2)
elif(numero3>numero1) and (numero3>numero2) and (numero2>numero4) and (numero2>numero5):
    print("El número mayor es", numero3)
elif(numero4>numero1) and (numero4>numero2) and (numero4>numero3) and (numero4>numero5):
    print("El número mayor es", numero4)
else:
    print("El número mayor es", numero5)