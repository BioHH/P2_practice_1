#!/usr/bin/python

#represents the sum of two numbers in a num
#my_sum: num, num -> num
# takes 2 num m and n respectively
# returns the sum of n + m
# input: 3,4 ; output: 7
# input: 5,4 ; output: 9
# input: 0, 0; output 0

def my_sum ():
    n = int(input ("Ingrese un numero n "))
    m = int(input ("Ingrese un numero m ")) 
    
    print(n + m)

#represents the rest of two numbers in a num
#my_rest: num, num -> num
# takes 2 num m and n respectively
# returns the rest of n - m
# input: 4,3 ; output: 1
# input: 20,8 ; output: 12
# input: 9, 10; output -1

def my_rest ():
    n = int(input ("Ingrese un numero n "))
    m = int(input ("Ingrese un numero m ")) 
    
    print(n - m)

#represents the product of two numbers in a number
#my_product: num, num -> num
# takes 2 num m and n respectively
# returns the product of n * m
# input: 3,4 ; output: 12
# input: 5,4 ; output: 20
# input: 0, 0; output 0

def my_product ():
    n = int(input ("Ingrese un numero n "))
    m = int(input ("Ingrese un numero m ")) 
    
    print(n * m)

#represents the division of two numbers in a float
#my_division: num, num -> num
# takes 2 num m and n respectively
# returns the division of n / m
# input: 3,4 ; output: 7
# input: 5,4 ; output: 9
# input: 0, 0; output 0

def my_division ():
    n = int(input ("Ingrese un numero n "))
    m = int(input ("Ingrese un numero m ")) 
    
    print(n / m)

o = int (input(" 1. Sum \n 2. Rest \n 3. Product \n 4. Division \n "))

def option (o):

    if o == 1:
        my_sum()
    elif o == 2:
        my_rest()  
    elif o ==3:
        my_product()
    else:
        my_division()

    l = int(input ("5. Salir "))

    if l == 5:
        return
    else:
        option (o)

option(o)

