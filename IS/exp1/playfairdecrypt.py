def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText 


def generateKeyTable(key):
    keySquare = [["" for i in range(5)] for i in range(5)]

    key_index = 0

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphakey = [char for char in alphabet if char not in key]


    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                keySquare[i][j] = key[key_index]
                key_index += 1
            else:
                keySquare[i][j] = alphakey[0]
                alphakey = alphakey[1:]
    
    return(keySquare)

# diagraph 
def diagraphGenerator(ciphertext):
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = removeSpaces(ciphertext)
    diagraph_list = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    return(diagraph_list) 

def find2DIndex(value, table):
    for row_index, row in enumerate(table):
        for col_index, element in enumerate(row):
            if element == value:
                return row_index, col_index
    return None

def negmod5(num):
    if num < 0:
        num += 5
    return num % 5

def columnDecryption(en_char1, en_char2, keyTable):
    char1 = keyTable[negmod5(en_char1[0]-1)][en_char1[1]]
    char2 = keyTable[negmod5(en_char2[0]-1)][en_char2[1]]
    return char1 + char2

def rowDecryption(en_char1, en_char2, keyTable):
    char1 = keyTable[en_char1[0]][negmod5(en_char1[1]-1)]
    char2 = keyTable[en_char2[0]][negmod5(en_char2[1]-1)]
    return char1 + char2

def rectangularDecryption(en_char1, en_char2, keyTable):
    char1 = keyTable[en_char1[0]][en_char2[1]]
    char2 = keyTable[en_char2[0]][en_char1[1]]
    return char1 + char2


def playfairDecrypt(en_diagraph_list, keyTable):
    diagraphs = []
    for diagraph in en_diagraph_list:
        char1 = find2DIndex(diagraph[0], keyTable)
        char2 = find2DIndex(diagraph[1], keyTable)
        if char1[1] == char2[1]: # same column
            diagraphs.append(columnDecryption(char1, char2, keyTable))
        elif char1[0] == char2[0]: # same row
            diagraphs.append(rowDecryption(char1, char2, keyTable))
        else:
            diagraphs.append(rectangularDecryption(char1, char2, keyTable))

    return diagraphs


ciphertext = input("Cipher Text: ")
en_diagraph_list = diagraphGenerator(ciphertext)

# correct format of key and keytable
key = input("Key: ")
key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
keyTable = generateKeyTable(key)

diagraphs = playfairDecrypt(en_diagraph_list, keyTable)
decrypted = ""
for diagraph in diagraphs:
    decrypted += diagraph

print("Plain Text: ", decrypted.lower())

