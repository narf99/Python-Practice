import random

def formatNum(numToFormat):
    """This formats a number to 2 decmail places"""

    for I in range(len(numToFormat)):
        if numToFormat[I] == ".":
            while len(numToFormat)-I < 3:
                numToFormat += "0"

    return numToFormat

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

numOfStocks = getMin(input("How many stocks do you want in your portfolio?\n: "), 1)

stocks = []

for i in range(numOfStocks):
    stocks.append([input("Please enter the 3 letter symbol\n: "), input("Please enter the company name\n: "), getMin(input("How many shares would you like?\n: ")), float(format(random.randrange(1, 201) + random.random(), ".2f"))])
    stocks[i].append(stocks[i][2] * stocks[i][3])

for i in range(numOfStocks):

    stocks[i][3] = formatNum(str(stocks[i][3]))
    stocks[i][4] = formatNum(str(stocks[i][4]))

    print("Symbol: " + stocks[i][0] + " | Company Name: " + stocks[i][1] + " | Price: $" + stocks[i][3] + " | Total Shares: " + str(stocks[i][2]) + " | Total Value: $" + str(stocks[i][4]))