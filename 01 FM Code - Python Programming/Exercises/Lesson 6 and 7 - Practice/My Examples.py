def pizza_needed():
    people = input ("how many people will you be coming ? :")
    num_slice =input ('How many scices with each person eats :')
    total_num = people * num_slice
    print (" They will be  " + people + " invited ")
    print ("You will need " + total_num + " pizza slices")
pizza_needed()






user_one = int(input ("Enter your lucky number : "))
user_two = int( input ("Guess the number enter by userone : "))

while user_two != user_one :
    if user_two < user_one :
        print ("Please guess higher !")
    elif user_two > user_one :
        print ("Plase guess lower !" )
    
    user_two =  int( input ("Guess again : "))
print ("Nailed it ")