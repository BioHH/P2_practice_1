#!/usr/bin/python

#Imprimir n números naturales pares 
# naturalesN: int -> string
#toma un numero
#devuelve los numeros pares hasta ese numero
#entrada: 10, salida: "0,2,4,6,8,10"
#entrada: 20, salida: "0,2,4,6,8,10,12,14,16,18,20"
#entrada: 5, salida: "0,2,4"

n = int (input ("Ingrese un número "))
def naturalesN (n):
    if 0 == n:
        print ("0")
    else:
        if (n % 2) == 0:
            print (n)
            naturalesN (n - 1)
        else:
            naturalesN (n - 1)

naturalesN(n)
