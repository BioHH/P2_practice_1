#!/usr/bin/python

# A sum of numbers between n and m using recursivity
# Summation: int, int -> int
# takes two numbers n and m respectively
# gives the summation of all numbers between n and m
# input: 1,50 ; output: 1275
# input: 1,20 ; output: 210
# input; 10,70 ; output: 3115

n = int (input ("Ingrese el valor de n "))
m = int (input ("Ingrese el valor de m "))

def Summation(n, m, c = 0, s = 0):
    if c != m:
        s = s + n
        Summation(n + 1, m, c + 1, s)
    else:
        print (s)

Summation (n,m)
