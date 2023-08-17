import random

class Player():
    def __init__(self):
        global allItems
        self.gold = 200 + random.randrange(0,201)
        self.items = []

        for _ in range(4):
            self.items.append(allItems[random.randrange(len(allItems))])
    
    def buyItem(self, item):
        self.items.append(item)
        self.gold -= item.price

    def sellItem(self, item):
        # find the item we are selling and remove it
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items.pop(i)
                break
        
        self.gold += item.price

class Shop():
    def __init__(self):
        self.inventory = []
        self.gold = 1000 + random.randrange(0,201)
    
    def sellItem(self, item):
        # find the item we are selling and remove it
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                self.inventory.pop(i)
                break
        
        self.gold += item.price
    
    def buyItem(self, item):
        self.inventory.append(item)
        self.gold -= item.price
    
    def randomizeInventory(self, items:list):
        self.inventory = []
        for _ in range(10):
            self.inventory.append(items[random.randrange(len(items))])

class Item():
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

def display():
    global player
    global shop
    print("Player" + "\t" + "Gold: " + str(player.gold) + "\t\t\t\t" + "Shop" + "\t" + "Gold: " + str(shop.gold))
    print("Inventory:" + "\t\t\t\t\t" + "Inventory:")
    print("#" + "\t" + "Name" + "\t\t\t" + "Price" + "\t\t" + "#" + "\t" + "Name" + "\t\t\t" + "Price")

    display=[]

    for i in range(len(player.items)):
        display.append(str(i+1) + "\t" + standardizeLength(player.items[i].name, 19) + "\t" + str(player.items[i].price))


    for i in range(len(shop.inventory)):
        if i<len(player.items):
            display[i] +="\t\t" + str(i+1) + "\t" + standardizeLength(shop.inventory[i].name, 19) + "\t" + str(shop.inventory[i].price)
        
        else:
            display.append("\t\t\t\t\t\t" + str(i+1) + "\t" + standardizeLength(shop.inventory[i].name, 19) + "\t" + str(shop.inventory[i].price))

    for i in range(len(display)):
        print(display[i])

def standardizeLength(string:str, length:int) -> str:
    """this lengthens or shortens strings"""

    # this lengthens the string
    while len(string)<length:
        string+=" "
    
    # this shortens the string
    if len(string)>length:
        string=string[0:length]

    return string

def getUserInput(question:str) -> (str | bool):
    """This gets user input from the user expecting that you want a string if you want an int use something different"""
    
    # this generates the options list
    def createOptions(question):

        options = question.split("(")
        indexesToRemove = []

        for i in range(len(options)):
            
            options[i] = options[i].split(")")
            
            for I in range(len(options[i])):
                
                if len(options[i][I]) > 1:
            
                    options[i].pop(I)
            
            if len(options[i]) < 1:
            
                indexesToRemove.append(i)
        
        # get rid of empty indexes
        for i in range(len(indexesToRemove)):
            
            options.pop(indexesToRemove[i])
        
        # unnest the options
        for i in range(len(options)):
            
            options[i] = options[i][0]
        
        return options
    
    options = createOptions(question)

    # find what the user wants to do
    whatToDo = input(question+" \n: ")

    # make sure the user inputed what the programmer wanted
    while whatToDo not in options:
            
        # ask again if its not
        whatToDo = input("I don't understand " + question + " \n: ")
        
    # return what the user wants to do
    return whatToDo

def getNumFromUser(minNum:int, maxNum:int, num = "", values = None) -> int:
    """Min and max numbers are inclusive. num and values are for recursive function calls"""
    
    # make the list holding the right values this is in a if statment so we dont have to recreate the list ever recursive call
    if values == None:
        values = []
        for i in range(minNum, maxNum+1):
            values.append(str(i))
    
    # get the number from the user and make sure its actually a number
    num = input("Please input a number from " + str(minNum) + " to " + str(maxNum) + " \n: ")
    while num not in values:
        num = input("Please input a number from " + str(minNum) + " to " + str(maxNum) + " \n: ")
    
    # make sure its the right number
    for i in range(minNum, maxNum+1):
        if int(num) == i:
            return i
    
    return getNumFromUser(minNum, maxNum, num, values)

allItems = [
    Item("Abucuss", 2), Item("Acid", 25), Item("Airship", 20000), Item("Alchimests Fire", 50), Item("Alchimests Supplies", 50),
    Item("Alexandrite", 500), Item("Amber", 100), Item("Amethyst", 100), Item("Amulet", 5), Item("Battle Axe", 10),
    Item("Short Sword", 5), Item("Long Sword", 10), Item("Great Axe", 20), Item("Great Sword", 20), Item("Hand Axe", 5)
]

shop = Shop()
shop.randomizeInventory(allItems)

player = Player()

display()

whatDo = getUserInput("What would you like to do? (b)uy an item, (s)ell an item, (q)uest, or (e)xit? ")

while whatDo!="e":
    # it is possible to soft lock yourself when buying or selling but it will probably not happen in reality
    while whatDo == "b":
        print("Which item would you like to buy? ")
        itemIndex = getNumFromUser(1, len(shop.inventory))-1

        if player.gold > shop.inventory[itemIndex].price:
            player.buyItem(shop.inventory[itemIndex])
            shop.sellItem(shop.inventory[itemIndex])
            break

        else:
            print("Not enough gold")
    
    while whatDo == "s":
        print("Which item would you like to sell? ")
        itemIndex = getNumFromUser(1, len(player.items))-1

        if shop.gold > player.items[itemIndex].price:
            shop.buyItem(player.items[itemIndex])
            player.sellItem(player.items[itemIndex])
            break

        else:
            print("Not enough gold")
    
    if whatDo == "q":
        goldToAdd = 20+random.randrange(0,21)
        print(str(goldToAdd) + " gold collected")
        player.gold += goldToAdd
        shop.randomizeInventory(allItems)
    
    display()

    whatDo = getUserInput("What would you like to do? (b)uy an item, (s)ell an item, (q)uest, or (e)xit? ")
