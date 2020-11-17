# PRÁCTICA 4 --> EJERCICIO 5
# Pida al usuario un importe en euros y diga si el cajero automático le 
# puede dar dicho importe utilizando el mismo billete y el más grande 	
# (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).

importe = int(input("Ponga un importe: "))

if(importe%500 == 0): 
# Queremos saber el resto de 500 para saber si podemos coger
# ese billete y no nos sobre dinero.
    cajero = importe / 500
# Si el resto es 0 es que no nos sobra dinero y es el billete
# más grande, así que dividimos el importe entre el billete
# para saber que cantidad de ese billete dar.
    print("El cajero le devuelve", cajero, "billetes de 500€") 
elif(importe%200 == 0):
    cajero = importe / 200
    print("El cajero le devuelve", cajero, "billetes de 200€")
elif(importe%100 == 0):
    cajero = importe / 100
    print("El cajero le devuelve", cajero, "billetes de 100€")
elif(importe%50 == 0):
    cajero = importe / 50
    print("El cajero le devuelve,", cajero, "billetes de 50€")
elif(importe%20 == 0):
    cajero = importe / 20
    print("el cajero le devuleve,", cajero, "billetes de 20€")
elif(importe%10 == 0):
    cajero = importe / 10
    print("el cajero le devuleve,", cajero, "billetes de 10€")
elif(importe%5 == 0):
    cajero = importe / 5
    print("el cajero le devuleve,", cajero, "billetes de 5€")