# key table
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
def diagraphGenerator(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = removeSpaces(plaintext)
    clean_text = []
    i = 0
    
    while i < len(plaintext):
        clean_text.append(plaintext[i])
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i+1]:
                clean_text.append("X")
            else:
                clean_text.append(plaintext[i+1])
                i += 1
        elif len(clean_text) % 2 != 0:
            clean_text.append('Z')
        i+=1
    
    diagraph_list = [clean_text[i:i+2] for i in range(0, len(clean_text), 2)]
    return(diagraph_list) 


def find2DIndex(value, table):
    for row_index, row in enumerate(table):
        for col_index, element in enumerate(row):
            if element == value:
                return row_index, col_index
    return None
    
# column encrypt
def columnEncryption(char1, char2, keyTable):
    en_char1 = keyTable[(char1[0]+1)%5][char1[1]]
    en_char2 = keyTable[(char2[0]+1)%5][char2[1]]
    return en_char1 + en_char2

# row encrypt
def rowEncryption(char1, char2, keyTable):
    en_char1 = keyTable[char1[0]][(char1[1]+1)%5]
    en_char2 = keyTable[char2[0]][(char2[1]+1)%5]
    return en_char1 + en_char2

# rectangular encrypt
def rectangularEncryption(char1, char2, keyTable):
    en_char1 = keyTable[char1[0]][char2[1]]
    en_char2 = keyTable[char2[0]][char1[1]]
    return en_char1 + en_char2


def playfairEncrypt(diagraph_list, keyTable):
    encrypted_diagraphs = []
    for diagraph in diagraph_list:
        char1 = find2DIndex(diagraph[0], keyTable)
        char2 = find2DIndex(diagraph[1], keyTable)
        if char1[1] == char2[1]: # same column
            encrypted_diagraphs.append(columnEncryption(char1, char2, keyTable))
        elif char1[0] == char2[0]: # same row
            encrypted_diagraphs.append(rowEncryption(char1, char2, keyTable))
        else:
            encrypted_diagraphs.append(rectangularEncryption(char1, char2, keyTable))

    return encrypted_diagraphs


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText 


# correct format of plaintext and diagraphs
plaintext = input("Plain Text: ")
diagraph_list = diagraphGenerator(plaintext)


# correct format of key and keytable
key = input("Key: ")
key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
keyTable = generateKeyTable(key)


encrypted_diagraphs = playfairEncrypt(diagraph_list, keyTable)
encrypted = ""
for diagraph in encrypted_diagraphs:
    encrypted += diagraph

print("Cipher Text: ", encrypted.lower())

