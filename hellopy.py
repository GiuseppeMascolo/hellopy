# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:26:19 2017

@author: Giuseppe Mascolo
from: https://www.youtube.com/watch?v=N4mEzFDjqtA
"""

import random
import sys
import os

# First Python program
'''
Multiline comment
'''

print("Hello World")

name = "Derek"
print(name)

'''
There are 4 main types:
    Numbers, Strings, Lists[], Tuples(), Dictionaries{}
7 algorithmical operators:
    + - * /  %(module)  **(exponential)  //(floor division)  
    moltiplication and division are done before addition and subtraction

'''
print("7 + 2 = ", 7+2)
print("7 - 2 = ", 7-2)
print("7 * 2 = ", 7*2)
print("7 / 2 = ", 7/2)
print("7 % 2 = ", 7%2)
print("7 ** 2 = ", 7**2)
print("7 // 2 = ", 7//2)

print("1 + 2 - 3 * 2 = ", 1+2-3*2)
print("(1 + 2 - 3) * 2 = ", (1+2-3)*2)

quote = "\"where there's a will, there's a way\""
multi_line_quote = ''' just
a multi line quote 
as always '''

new_string = quote + multi_line_quote
print(new_string)

print("%s %s %s" %("I like the quote", quote, multi_line_quote) )

print("I dont' like")
print("you")
print("I dont' like", end=" ")
print("you")


#Now let's create a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
print('First item:', grocery_list[0])
grocery_list[0] = 'Green juice'
print('First item:', grocery_list[0])

print('First 2 items:', grocery_list[0:2]) #item 3 not included

''' We can also create a list of lists 
    if then we make a change inside one of the lists
    those changes will stay also in the list of lists
'''
grocery_list.append("onions")
print(grocery_list)
grocery_list.insert(1,"Pickle")
grocery_list.remove("Bananas")
print(grocery_list)

'''there are many functions considering list as objects '''

del grocery_list[1]
print(grocery_list)

super_villains = {'Fiddle' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])

del super_villains['Fiddle']
print(super_villains)
print(len(super_villains))
print(super_villains.keys())
print(super_villains.values())

#Conditions
age = 21

if ( (age > 16) and (age < 21) ) :
    print("old")
elif age > 5 :
    print("young")
else :
    print("baby")

#Looping
for i in range(0, 10):
    print(i, ' ', end="")
print("ciao")
print('\n')
        
random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)
    
    
#functions
def addNumber(a, b):
    sam = a + b;
    return sam

print(addNumber(1,4))


#input from screen
print('What is your name')
nome = sys.stdin.readline ()

print('Hello', nome)