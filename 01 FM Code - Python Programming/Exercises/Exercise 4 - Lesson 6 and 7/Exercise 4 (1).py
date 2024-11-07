# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits =[ 'Orange',  'Grape', 'Banana' , 'Raspberry' ]
for fruit in fruits :
   print (fruit)

# TODO: Use a for loop to print each fruit in the list
print (fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
number = 5
while number > 1 :
   print (number)
   number = number - 1 

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range (1,11) :
   print(i * i)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
Colors =['Red' , 'Blue' , 'Green' , 'Purple ' ,' Orange']
# TODO: Use a for loop to select and print 3 random colors from the list
result = random.choice(Colors)
for color in range (3) :
   print(random.choice(Colors))
   
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
#import math_operations

def add(a, b):
    return a + b
print(add ( 6, 9))

def subtract(a, b):
    return a - b
print(subtract( 4 ,5))


def multiply(a, b):
    return a * b
print (multiply ( 4 , 3))

def divide(a, b):
    if b != 0:
        return a / b
print(divide ( 125 , 45))

# TODO: Use a while loop to create a simple calculator
while True :
 num1= int (input ("Enter value to number one : "))
 num2 = int (input ("Enter value to number two : "))

 operation =  input(" Which operation do you prefer (+ , - ,* ,/) :")

 if operation == '+':
    result = num1 + num2
    print( result)

 elif operation == '-':
    result = num1 - num2
    print(result)

 if  operation == '/'   :
  if  num2 == 0:
    print ("Division by zero not allowed")  
 else :
    result= num1 / num2
    print (result)
 if operation == '*':
    result = num1 * num2
    print (result)
 else:
    print("Invalid Input")
