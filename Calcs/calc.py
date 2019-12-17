#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:13:52 2019

@author: cooperast
"""

def sum(x,y):
	print(x + y)
def sub(x,y):
	print(x - y)
def multiply(x,y):	
	print(x * y)  
def division(x,y):	
	print(x / y)
def remainder(x,y):	
	print(x % y)
def power(x,y):
    print('\n'f'[{x**y}]')
def sqroot(x):
    print(f'[{x**0.5}]')
def cubrt(x):
    print(f'[{x**(1/3)}]')
def inverse(x):
    print(f'[{x**-1}]')

while True:
    user = int(input('\n'"What operation?"'\n''1: sum 2: sub 3: multiply 4: division 5: remainder ''\n''6: power 7: square root 8: cubic root 9: inverse ''\n' '0: EXIT ''\n'))
    if (user>=1 and user<=5):
        ask1 = float(input('Number 1: '))
        ask2 = float(input('Number 2: '))
        if user == 1:
            sum(ask1,ask2)
        elif user == 2:
            sub(ask1,ask2)
        elif user == 3:
            multiply(ask1,ask2)
        elif user == 4:
            division(ask1,ask2)
        elif user == 5:
            remainder(ask1,ask2)
    elif (user == 6):
        ask1 = float(input('Number: '))
        ask2 = float(input('Power raised to: '))
        if user == 6:
            power(ask1,ask2)
    elif (user>=7 and user<=8):
        ask1 = float(input('\n''Number: '))
        if user == 7:
            sqroot(ask1)
        if user == 8:
            cubrt(ask1)
    elif (user == 9):
        ask1 = float(input('\n''Number: '))
        if user == 9:
            inverse(ask1)
    elif (user == 0):
        exit()
        
    
    