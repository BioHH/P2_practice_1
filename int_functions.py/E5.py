#!/usr/bin/python

# Calcular e imprimir el resultado de la suma de los n primeros 
# numeros naturales
# n:sumaNaturales: int -> int
# toma un entero n
# devuelve la suma de los numeros naturales hasta n
#entrada: 50 ; salida: 1275
#entrada: 20 ; salida: 210
#entrada: 10 ; salida: 55

c = int (input ("Ingrese el valor de c "))

def n_sumaNaturales(c, n = 1, s = 0):
    if c != 0:
        s = s + n
        n_sumaNaturales(c - 1, n + 1, s)
    else:
        print (s)

n_sumaNaturales(c)
