#!/usr/bin/python

#gives a string n times duplicate
# duplicate_n: str , int -> str
# takes a string and a number n
# return the string duplicate n times
# input: tom, 3 ; output: tomtomtom
# input: alex, 5 ; output: alexalexalexalexalex
# input: agus, 0 ; output: (none)

s = input("Enter a string ")
n = int(input ("Enter a number n "))

def duplicate (s , n):
    print (s * n)

duplicate(s, n)


