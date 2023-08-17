import random
import copy

def getPosition(word):
    direction = random.randrange(0, 7)

    if direction == 0:
        position = [random.randrange(20), random.randrange(len(word), 20)]
    
    elif direction == 1:
        position = [random.randrange(0, 20 - len(word)), random.randrange(len(word), 20)]
    
    elif direction == 2:
        position = [random.randrange(0, 20 - len(word)), random.randrange(20)]
    
    elif direction == 3:
        position = [random.randrange(0, 20 - len(word)), random.randrange(0, 20 - len(word))]
    
    elif direction == 4:
        position = [random.randrange(20), random.randrange(0, 20 - len(word))]
    
    elif direction == 5:
        position = [random.randrange(len(word), 20), random.randrange(0, 20 - len(word))]
    
    elif direction == 6:
        position = [random.randrange(len(word), 20), random.randrange(0, 20)]
    
    elif direction == 7:
        position = [random.randrange(len(word), 20), random.randrange(len(word), 20)]
    
    return [position, direction]

def checkDirection(word:list):
    # for whatever reason copy isnt working so we are forced to have this stupid function
    def fixPos(word):
        if word[3] == 0: # up
            word[2] += len(word[0])
            
        elif word[3] == 1: # up right
            word[1] -= len(word[0])
            word[2] += len(word[0])
                
        elif word[3] == 2: # right
            word[1] -= len(word[0])
                
        elif word[3] == 3: # down right
            word[1] -= len(word[0])
            word[2] -= len(word[0])
                
        elif word[3] == 4: # down
            word[2] -= len(word[0])
            
        elif word[3] == 5: # down left
            word[1] += len(word[0])
            word[2] -= len(word[0])
                
        elif word[3] == 6: # left
            word[1] += len(word[0])
                
        elif word[3] == 7: # up left
            word[1] += len(word[0])
            word[2] += len(word[0])
              
    global wordSearch
    newPos = False

    for _ in range(0, 100):

        for I in range(len(word[0])):

            if wordSearch[word[2]][word[1]] != 0:
                position = getPosition(word[0])
                word = [word[0], position[0][0], position[0][1], position[1]]
                newPos = True
                I = 0
                break
            
            if word[3] == 0: # up
                word[2] -= 1
            
            elif word[3] == 1: # up right
                word[1] += 1
                word[2] -= 1
            
            elif word[3] == 2: # right
                word[1] += 1
            
            elif word[3] == 3: # down right
                word[1] += 1
                word[2] += 1
            
            elif word[3] == 4: # down
                word[2] += 1
            
            elif word[3] == 5: # down left
                word[1] -= 1
                word[2] += 1
            
            elif word[3] == 6: # left
                word[1] -= 1
            
            elif word[3] == 7: # up left
                word[1] -= 1
                word[2] -= 1

        if I == len(word[0])-1:
            if newPos == True:
                return [word[0], position[0][0], position[0][1], position[1]]
            
            else:
                fixPos(word)
                return word
    
    print("Maximum repeats reached")
    return None

wordsRaw = open("BPA C++ State 2019\SocStudy_Vocab.Teacher.txt", "r")

words = []
for i in range(int(wordsRaw.readline()[:-1])):
    words.append(wordsRaw.readline()[:-1])

wordsRaw.close()

wordSearchTitle = words[-1]

words.pop(-1)

wordSearch = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

directedWords = []
for i in range(len(words)):
    # place the words in the word search
    position = getPosition(words[i])
    directedWords.append([words[i], position[0][0], position[0][1], position[1]])

# place words
for i in range(len(directedWords)):
    
    directedWords[i] = checkDirection(directedWords[i])

    for I in range(len(directedWords[i][0])):
        
        wordSearch[directedWords[i][2]][directedWords[i][1]] = directedWords[i][0][I]

        if directedWords[i][3] == 0: # up
            directedWords[i][2] -= 1
            
        elif directedWords[i][3] == 1: # up right
            directedWords[i][1] += 1
            directedWords[i][2] -= 1
        
        elif directedWords[i][3] == 2: # right
            directedWords[i][1] += 1
        
        elif directedWords[i][3] == 3: # down right
            directedWords[i][1] += 1
            directedWords[i][2] += 1
        
        elif directedWords[i][3] == 4: # down
            directedWords[i][2] += 1
        
        elif directedWords[i][3] == 5: # down left
            directedWords[i][1] -= 1
            directedWords[i][2] += 1
        
        elif directedWords[i][3] == 6: # left
            directedWords[i][1] -= 1
        
        elif directedWords[i][3] == 7: # up left
            directedWords[i][1] -= 1
            directedWords[i][2] -= 1

wordSearchKey = copy.deepcopy(wordSearch)

# fill word search
for i in range(len(wordSearch)):
    for I in range(len(wordSearch[i])):
        if wordSearch[i][I] == 0:
            wordSearch[i][I] = random.choice(alphabet)
        
        if wordSearchKey[i][I] == 0:
            wordSearchKey[i][I] = " "

# prepare word search
wordSearchFinal = []
wordSearchKeyFinal = []
for i in range(len(wordSearch)):
    string = ""
    keyString = ""

    for I in range(len(wordSearch[i])):
        string += wordSearch[i][I].upper() + " "
        keyString += wordSearchKey[i][I] + " "
    
    wordSearchFinal.append(string)
    wordSearchKeyFinal.append(keyString)

# add word bank
for i in range(len(words)):
    try:
        wordSearchFinal[i] += "\t" + words[i]
        wordSearchKeyFinal[i] += "\t" + words[i]
    
    except IndexError:
        wordSearchFinal.append("\t\t\t\t\t\t" + words[i])
        wordSearchKeyFinal.append("\t\t\t\t\t\t" + words[i])

# display and save words
output = open("BPA C++ State 2019\word_search.txt", "w")
keyOutput = open("BPA C++ State 2019\word_search_key.txt", "w")

output.write("\t\t" + wordSearchTitle + "\n")
keyOutput.write("\t\t" + wordSearchTitle + "\n")

for i in range(len(wordSearchFinal)):
    output.write(wordSearchFinal[i] + "\n")
    keyOutput.write(wordSearchKeyFinal[i] + "\n")

output.close()
keyOutput.close()

print("Word search can be found in word_search.txt and word_search_key.txt")