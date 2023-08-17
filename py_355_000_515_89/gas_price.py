# Contestant Number: 00051589
import info

def get_discount(card_number):
    if card_number >= 1000 and card_number <= 4000:
        return 0.02
    
    elif card_number >= 4001 and card_number <= 7000:
        return 0.03

    elif card_number >= 7001 and card_number <= 9999:
        return 0.04

def get_user_input(question:str) -> str:
    """This gets user input from the user expecting that you want a string if you want an int use something different"""
    
    # this generates the options list
    def create_options(question):

        options = question.split("(")
        indexes_to_remove = []

        for i in range(len(options)):
            
            options[i] = options[i].split(")")
            
            for I in range(len(options[i])):
                
                if len(options[i][I]) > 1:
            
                    options[i].pop(I)
            
            if len(options[i]) < 1:
            
                indexes_to_remove.append(i)
        
        # get rid of empty indexes
        for i in range(len(indexes_to_remove)):
            
            options.pop(indexes_to_remove[i])
        
        # unnest the options
        for i in range(len(options)):
            
            options[i] = options[i][0]
        
        return options
    
    options = create_options(question)

    # find what the user wants to do
    what_to_do = input(question+" \n: ")

    # make sure the user inputed what the programmer wanted
    while what_to_do not in options:
            
        # ask again if its not
        what_to_do = input("I don't understand " + question + " \n: ")
        
    # return what the user wants to do
    return what_to_do

def get_min(user_input:str, min=1) -> int:
    """This function takes user input and returns a number from a minimum to infinity"""

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            user_input = int(user_input)

            break
        
        # if its not an integer get the input again
        except ValueError:
            user_input = input("Not a number please input a number bigger then " + str(min) + " ")
                
    
    # check if its the right number
    while user_input < min:
        user_input = input("Not the right number please input a number bigger then " + str(min) + " ")

        return get_min(user_input, min)

    return user_input

def get_num(user_input:str, min:int, max:int) -> int:
    """This function gets user input and returns a float from a given minimum to a maximum"""

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            user_input = int(user_input)

            break
        
        # if its not an integer get the input again
        except ValueError:
            user_input=input("Not a number please input a number from " + str(min) + " " + str(max) + " ")
                
    
    # check if its the right number
    while user_input > max or user_input < min:

        user_input = input("Not the right number please input a number from " + str(min) + " " + str(max) + " ")

        return get_num(user_input, min, max)
    
    return user_input

octanes = info.get_octanes()

# get what to do from the user
what_to_do = get_user_input("Would you like to use your discount (d), pump gas (p), or exit (x)?")

if what_to_do == "d":
    # get the specifc octane
    octane = info.get_octane(octanes)

    # get the discount card number
    card_number = get_num(input("What is the discount card number? "), 1000, 9999)

    # get the discounted price
    octane.discount(get_discount(card_number))

    # display the price of gas
    print(octane)

    # get the amount of gas
    gallons = input("How many gallons would you like to buy? ")

    gallons = get_min(gallons)

    # caculate and display the total cost of gass
    print("Your total cost of gass is: $" + str(info.round(gallons*octane.price, 2)))

elif what_to_do == "p":
    # get the specifc octane
    octane = info.get_octane(octanes)

    # display the price of gas
    print(octane)

    # get the amount of gas
    gallons = input("How many gallons would you like to buy? ")

    gallons = get_min(gallons)

    # display and caculate the total cost of gas
    print("Your total cost of gass is: $" + str(info.round(gallons*octane.price,2)))

print("Thank You; Please Come Again")