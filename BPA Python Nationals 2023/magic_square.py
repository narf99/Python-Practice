# Contestant Number: 00051589
"""This program takes a text document of squares and returns if they are magic or not"""

def is_magic_square(square:list):
    outcome = ""
    
    # rows
    rowTotals = []
    
    for i in range(len(square)):
        total = 0

        for I in range(len(square[i])):
          total += int(square[i][I])
        
        rowTotals.append(total)
    
    del(total)

    for i in range(len(square)):
        checkTotal = rowTotals[i]
        
        for I in range(len(square)):
            
            if checkTotal != rowTotals[I]:
                outcome = "NOT MAGIC: A row sum is incorrect"
    
    del(checkTotal)
    del(rowTotals)
    
    # colums
    columTotals = []

    for i in range(len(square)):
        total = 0

        for I in range(len(square[i])):
            total += int(square[I][i])
        
        columTotals.append(total)
    
    del(total)

    for i in range(len(square)):
        checkTotal = columTotals[i]
        
        for I in range(len(square)):
            
            if checkTotal != columTotals[I]:
                if outcome != "MAGIC":
                    outcome = "NOT MAGIC: Multiple sums incorrect"

                else:
                    outcome = "NOT MAGIC: A column sum is incorrect"
    
    del(checkTotal)
    del(columTotals)

    # diagonal and anti diagonal
    if outcome != "NOT MAGIC: Multiple sums incorrect":
        diagonalTotal = 0
        
        for i in range(len(square)):
            diagonalTotal += int(square[i][i])

        # anti diagonal
        antiDiagonalTotal = 0

        for i in range(len(square)-1, -1, -1):
            antiDiagonalTotal += int(square[i][i])
        
        if diagonalTotal != antiDiagonalTotal:
            outcome = "NOT MAGIC: Diagonal sums incorrect"

        del(diagonalTotal)
        del(antiDiagonalTotal)

    if outcome == "":
        outcome = "MAGIC"
    
    square.append(outcome)

    return square

numOfData = sum(1 for _ in open("PYTHON-00051589\magic.txt"))

data = open("PYTHON-00051589\magic.txt")
rawData = []

# get the raw data
for i in range(numOfData):
    rawData.append(data.readline()[:-1])

data.close()

del(numOfData)
del(data)

sortedData = []

# sort the data
for i in range(len(rawData)):
    set = []

    try: 
        rawData[i] = int(rawData[i])
    
    except:
        pass

    if type(rawData[i]) == int:
        for I in range(1, rawData[i]+1):
            set.append(rawData[i+I].split(" "))
        
    
    if set != []:
        sortedData.append(set)

del(set)
del(rawData)

# test the data
squares = []
for i in range(len(sortedData)):
    squares.append(is_magic_square(sortedData[i]))

del(sortedData)

# save the data
results = open("PYTHON-00051589/results.txt", "w")

for i in range(len(squares)):
    
    for I in range(len(squares[i])):
        if type(squares[i][I]) != str:
            
            for x in range(len(squares[i][I])):
                results.write(str(squares[i][I][x]) + " ")
            
            results.write("\n")
        
        else:
            results.write(squares[i][I] + "\n")
            results.write("\n")

results.close()