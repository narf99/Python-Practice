def encryption(words:list):
    table = {
        65:75, 66:76, 67:77, 68:78, 69:79, 70:80, 71:81, 72:82, 
        73:83, 74:84, 75:85, 76:86, 77:87, 78:88, 79:89, 80:90,
        81:65, 82:66, 83:67, 84:68, 85:69, 86:70, 87:71, 88:72,
        89:73, 90:74,
        97:107, 98:108, 99:109, 100:110, 101:111, 102:112, 103:113,
        104:114, 105:115, 106:116, 107:117, 108:118, 109:119, 110:120,
        111:121, 112:122, 113:97, 114:98, 115:99, 116:100, 117:101,
        118:102, 119:103, 120:104, 121:105, 122:106
    }

    for i in range(len(words)):
        
        words[i] = words[i][::-1].translate(table)

    return words

def decryption(words:list):
    table = {
        75:65, 76:66, 77:67, 78:68, 79:69, 80:70, 81:71, 82:72, 
        83:73, 84:74, 85:75, 86:76, 87:77, 88:78, 89:79, 90:80,
        65:81, 66:82, 67:83, 68:84, 69:85, 70:86, 71:87, 72:88,
        73:89, 74:90,
        107:97, 108:98, 109:99, 110:100, 111:101, 112:102, 113:103,
        114:104, 115:105, 116:106, 117:107, 118:108, 119:109, 120:110,
        121:111, 122:112, 97:113, 98:114, 99:115, 100:116, 101:117,
        102:118, 102:119, 104:120, 105:121, 106:122
    }

    for i in range(len(words)):
        
        words[i] = words[i][::-1].translate(table)
    
    return words

wordsRaw = open("Python 2021\plainText.txt")

word = wordsRaw.readline()

words = []

while word != "":
    words.append(word[:-1])

    word = wordsRaw.readline()

del(wordsRaw, word)

encryptedWords = encryption(words)

del(words)

decryptedWords = decryption(encryptedWords.copy())

print("Encrypted Words")
for i in range(len(encryptedWords)):
    print(encryptedWords[i])

print()

output = open("Python 2021\decryptedWords.txt","w")

print("Decrypted Words")
output.write("Decrypted Words\n")

for i in range(len(decryptedWords)):
    print(decryptedWords[i])
    output.write(decryptedWords[i] + "\n")

output.close()
del(output)

del(decryptedWords, encryptedWords)

input("Press enter to exit")