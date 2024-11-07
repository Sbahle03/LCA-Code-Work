# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input( " what is your name ? ")

# TODO: Ask the user for their age and store it in a variable
age = input ( "How old are you ? ")

# TODO: Print a greeting using the name and age variables
greeting = " Hello " + name + " you are  " +  age  + ' years old '+ ' you are so young '
print ( greeting)

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input  ( " what is the length of a rectangle ? "))

# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int( input( 'what is th width of the rectangle ? ')) 
# TODO: Calculate the area of the rectangle
area = length * width

# TODO: Print the result
print (area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temp_c = float(input("What is the temprature today ? "))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
temperature_f = round(( temp_c *  9/5 ) + 32, 2)
                    

# TODO: Print the result rounded to two decimal places
print ( temperature_f)