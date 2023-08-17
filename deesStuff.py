"""These are just my useful functions"""

def standardizeLength(string:str, length:int) -> str:
    """this lengthens or shortens strings"""

    # this lengthens the string
    while len(string)<length:
        string+=" "
    
    # this shortens the string
    if len(string)>length:
        string=string[0:length]

    return string

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

# TODO i feel like this could be better some how. it seems ineffecient right now
def getUserInput(question:str, bool=False, options=False, upper=False) -> (str | bool):
    """This gets user input from the user expecting that you want a string if you want an int use something different"""
    
    # this generates the options list
    def createOptions(question, upper):

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
        
        # add the options taken to capitals
        if upper == True:

            for i in range(len(options)):
            
                options.append(options[i].upper())
        
        return options
    
    if bool == False:
        
        options = createOptions(question, upper)

        # find what the user wants to do
        whatToDo = input(question+" \n: ")

        # make sure the user inputed what the programmer wanted
        while whatToDo not in options:
            
            # ask again if its not
            whatToDo = input("I don't understand " + question + " \n: ")
        
        # return what the user wants to do
        return whatToDo
    
    if bool == True:
        options = ["t","f"]

        # find what the user wants to do
        whatToDo = input(question + " \n: ")

        # make sure the user inputed what the programmer wanted
        while whatToDo not in options:
            
            # ask again if its not
            whatToDo = input("I don't understand " + question + " \n: ")
        
        if whatToDo == "t":
            
            return True
        
        elif whatToDo == "f":
            
            return False

def displayList(list:list, header:str) -> None:
    """This displays a list it assumes the values inside the list are objects with a specified string format matching the header"""
    
    # display the header
    print(header)
    
    # go through all the values in the list
    for i in range(len(list)):

        # dislay the number and the object string
        print(str(i+1)+"\t"+list[i].__str__())
    
def round(numToRound:float, placesToRoundTo=0, string=True) -> (str | int):
    """ this rounds a given number. doesn't round 5 up and the number of places to round to means the number of decmile places you want"""
    
    if string == True:
        return format(numToRound,".{}f".format(placesToRoundTo))
    
    else:
        return int(format(numToRound,".{}f".format(placesToRoundTo)))

def removeLastCharacters(stringToModify:str, numOfCharactersToRemove:int) -> str:
    """This removes a specific number of characters from the end of a string"""

    return stringToModify[:-numOfCharactersToRemove+1]

def translator(words:str, table:dict) -> str:
    """This function translates a string of letters based on a given table"""
    translatedWords = ""

    # this translates the words
    for translateWords in range(len(words)):
        translatedWords+=((words[translateWords][::-1].translate(table)))
    
    return translatedWords

def checkForStuff(userInput:str, limiter:int, Type=True, limiter2=1) -> (int | float):
    """
        This function returns user input. either an integer up to a max, minimum, or a float in between a max and a min 

        For a min number pass 2 arguments \n
        userInput = the input you get from the user \n
        limiter = minimum number

        for a max number pass 3 arguments \n
        userInput = the input you get from the user \n
        limiter = maximum number \n
        Type = False (to tell the program you are passing a max) \n

        for a float pass all 5 arguments \n
        userInput = the input you get from the user \n
        limiter = minimum number \n
        Type = None (To tell the program you want a float) \n
        limiter2 = maximimum number
    """

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            if Type != None:
                userInput = int(userInput)
            
            elif Type == None:
                userInput = float(userInput)

            break
        
        # if its not an integer get the input again
        except ValueError:
            
            if Type == True: # min
                
                userInput=input("Not a number please input a number bigger then " + str(limiter) + " ")
            
            elif Type == False: # max
                
                userInput=input("Not a number please input a number smaller then " + str(limiter) + " ")
            
            elif Type == None: # float
                
                userInput=input("Not a number please input a number from " + str(limiter) + " " + str(limiter2) + " ")
                
    
    # check if its the right number
    # Min
    if Type == True:
        
        while userInput < limiter:

            userInput = input("Not the right number please input a number bigger then " + str(limiter) + " ")

            return checkForStuff(userInput, limiter)
    
    # Max
    if Type == False:

        while userInput > limiter:

            userInput = input("Not the right number please input a number smaller then " + str(limiter) + " ")

            return checkForStuff(userInput, limiter, min)

    # float
    if Type == None:
        while userInput > limiter2 or userInput < limiter:

            userInput = input("Not the right number please input a number from " + str(limiter) + " " + str(limiter2) + " ")

            return checkForStuff(userInput, limiter, min, limiter2)
    
    return userInput

# these next 3 functions are seperated versions of the checkForStuff function
def getMin(userInput:str, min=1) -> int:
    """This function takes user input and returns a number from a minimum to infinity"""

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            userInput = int(userInput)

            break
        
        # if its not an integer get the input again
        except ValueError:
            userInput = input("Not a number please input a number bigger then " + str(min) + " ")
                
    
    # check if its the right number
    while userInput < min:
        userInput = input("Not the right number please input a number bigger then " + str(min) + " ")

        return getMin(userInput, min)

    return userInput

def getMax(userInput:str, max:int) -> int:
    """This function takes user input and returns a number smaller then a given max"""

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            userInput = int(userInput)

            break
        
        # if its not an integer get the input again
        except ValueError:
            userInput = input("Not a number please input a number smaller then " + str(max) + " ")
                
    
    # check if its the right number
    while userInput > max:
        userInput = input("Not the right number please input a number smaller then " + str(max) + " ")

        return getMax(userInput, max)

    return userInput

def getFloat(userInput:str, min:int, max:int) -> float:
    """This function gets user input and returns a float from a given minimum to a maximum"""

    # this changes the user input to an integer
    while True:
        
        # try to change the input to an integer
        try:
            userInput = float(userInput)

            break
        
        # if its not an integer get the input again
        except ValueError:
            userInput=input("Not a number please input a number from " + str(min) + " " + str(max) + " ")
                
    
    # check if its the right number
    while userInput > max or userInput < min:

        userInput = input("Not the right number please input a number from " + str(min) + " " + str(max) + " ")

        return getFloat(userInput, min, max)
    
    return userInput

def isNumPalindrom(x:int):
    """This function checks to see if a number is a palindrom"""
    return str(x)[::-1] == str(x)

def romanToInt(s: str) -> int:
    """This function converts a roman numeral to a number"""
    romanToIntDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, 
                      "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    integer = 0
    
    i = 0
    while i < len(s):
        try :
            integer += romanToIntDict[s[i] + s[i+1]]
            i += 2
            continue

        except:
            pass

        integer += romanToIntDict[s[i]]
        
        i += 1

    return integer

def moveValues(nums:list, value) -> None:
    """This function moves a specified value to the end of a list"""
    for i in range(nums.count(value)):
        nums.remove(value)
        nums.append(value)

# use this to find the length of a text document
# sum(1 for _ in open(fileName))