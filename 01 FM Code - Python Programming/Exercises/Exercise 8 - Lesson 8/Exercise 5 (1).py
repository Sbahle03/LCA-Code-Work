# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = [ "Apple " , "Banana"  , "Orange" , " Watermelon"]

# TODO: Add a fruit to the end of the list
fruits.append( 'Blueberry')
print (fruits)

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0,"Cherry")
print(fruits)
# TODO: Remove a fruit from the list
fruits.remove("Banana")


# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [ 1 , 2 , 3 , 4 ,5]

# TODO: Create a new list with each number squared
numbers_squred = [1  ,  4  ,9 , 16 , 25 ]
# TODO: Find the sum and average of the original numbers
sum_result =sum(numbers)

# TODO: Print the results
print (sum_result)
#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
Countries = {
    " South Africa" : "Cape Town" ,
    " Namibia"      : "Windhoek",
    " Sudan"        : "Khartoum",
    " USA"          : "Washington, DC"

}
# TODO: Add a new country-capital pair
new_key = "Angola "
new_value = "Luanda"
Countries[new_key] =new_value

print(Countries)

# TODO: Update the capital of an existing country
Countries.update({" South Africa" :" Pretoria ",})
print(Countries)

# TODO: Remove a country-capital pair
del Countries[" USA"]

# TODO: Print the modified dictionary
print(Countries)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits_colors = {
    "Orange"     : "Orange" ,
    "Blueberry"  : "Blue" ,
    "Apple"      : "Red" ,
    "Watermelon" : "Green",
    "Kiwi"       : "Brown"
}
# TODO: Print all the fruits (keys)
print (fruits_colors.keys())
# TODO: Print all the colors (values)
print(fruits_colors.values ())
# TODO: Print each fruit and its color
print(fruits_colors) 
# TODO: Check if a fruit is in the dictionary and print its color
if "Watermelon" in fruits_colors :
    print("Watermelon")
else : 
    print("The Key does not exist")