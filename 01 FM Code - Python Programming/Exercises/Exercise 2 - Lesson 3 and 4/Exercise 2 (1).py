# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 3
x += 3

# TODO: Multiply y by 2 using the *= operator
y = 2
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y

# TODO: Print the value of 'result'
print( result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 4
b = 3

if  a  >  b :
    print (" a is greater then b ")
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b = 3

if b % 2 == 0 :
    print ("b is even to 3 ")
# TODO: Create a condition that checks if c is less than or equal to a
c = 4

if c <= a :
    print ('c is equal to a')
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:

#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a > b) or  (b == 3 and c <= a ) 

if  (a > b) :
    print ("True")
else:
    print ("False")

if (b == 3) :
    print (" Even")
else :
    print ("Odd")

if c <= a :
    print ("True")
else: 
    print ("False")
     

# TODO: Print the value of 'final_condition'
print (final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int (input (" What is your test score ? "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
A= 90-100
B= 80-89 
C= 70-79
D= 60-69 
F= "Below 60"

if 90 <= score <= 100 :
    print('distinction') 
elif 80 <= score <= 89:
    print ('B pass')
elif 70 <= score <= 79:
    print ("C pass")
elif 60 <= score :
    print("D pass")
else : 
    print ("Test failed")

# TODO: Print the grade for the given score
#All in the code 
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1= int (input ("Enter value to number one : "))
num2 = int (input ("Enter value to number two : "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation =  input(" Which operation do you prefer (+ , - ,* ,/) :")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == '+':
    result = num1 + num2
    print( result)
elif operation == '-':

    result = num1 - num2

    print(result)
elif operation == '/'   :
    if num2 == 0:
        print ("Division by zero not allowed")  
else :
    result= num1 / num2
    print (result)
if operation == '*':
    result = num1 * num2
    print (result)
else:
    print("Error")
# TODO: Handle the case of division by zero
# All in the code

# TODO: Print the result of the operation
print( result)