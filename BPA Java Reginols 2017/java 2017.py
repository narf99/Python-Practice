itemsCosts = (2, 1, 3, 1, .75, .5)
devOptions = ("a", "b", "c", "d", "e", "f", "g", "h", "x")

numOfItems = 0
total = 0

def display():
    # TODO rewrite this it feels like it sucks
    global numOfItems
    global total

    print("\t\t\tCurrent Sales")
    print("Items Selected: " + str(numOfItems))
    print("Total: $" + str(total))
    print()

    print("\t\t\tSchool Vending Menu")
    print("A: Notebook Paper - $2.00\tB: Mechanical Pencils (3 Pack)    - $1.00")
    print("C: 3 Ring Binder  - $3.00\tD: Pens (3 Pack Black, Red, Blue) - $1.00")
    print("E: Folder         - $0.75\tF: Highlighter                    - $0.50")
    print("G: Clear Transasction\t\tH: Exit and Pay")
    print("X: Cancel and Exit")

def getUserInput(question:str, options:list) -> (str | bool):
    """This gets user input from the user"""
    userOptions = []
    for i in range(len(options)): # this allows for both uppercase and lower case to be given by the user
        userOptions.append(options[i].upper())
        userOptions.append(options[i])
    
    # find what the user wants to do
    whatToDo = input(question+" \n: ")

    # make sure the user inputed what the programmer wanted
    while whatToDo not in options:
        
        # ask again if its not
        whatToDo = input("I don't understand " + question + " \n: ")
    
    # return what the user wants to do
    return whatToDo.lower()

display()

whatDo = getUserInput("What would you like to buy?", devOptions)

while whatDo != "x":
    
    for i in range(6):
        if whatDo == devOptions[i]:
            numOfItems += 1
            total += itemsCosts[i]
    
    if whatDo == "g":
        numOfItems = 0
        total = 0

    elif whatDo == "h":
        print("Final Sales")
        print("Number of Items: " + str(numOfItems))
        print("Total: $" + str(total))
        exit()
    
    display()
    whatDo = getUserInput("What would you like to buy?", ["A", "B", "C", "D", "E", "F", "G", "H", "X", "a", "b", "c", "e", "d", "f", "g", "h", "x"])
