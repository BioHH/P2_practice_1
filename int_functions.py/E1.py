#!/usr/bin/python

#Imprimir los primeros 25 números naturales pares
# naturales25: string -> string
#No toma ningun valor
#Devuelve los primeros 25 naturales
# entrada: none, salida: "2, 4, 6, ...., 24"

def naturales25 (n = 25):
    if 0 == n:
        print ("Fin")
    else:
        if (n % 2) == 0:
            print (n)
            naturales25 (n - 1)
        else:
            naturales25 (n - 1)

naturales25()
