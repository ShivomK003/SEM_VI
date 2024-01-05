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
            clean_text.append('X')
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
def columnEncryption(diagraph, keyTable):
    ciphertext = ""
    char1 = find2DIndex(diagraph[0], keyTable)
    char2 = find2DIndex(diagraph[1], keyTable)
    return char1, char2

plaintext = "instruments"
key = "monarchy"

# correct format of key
key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
keyTable = generateKeyTable(key)
print(columnEncryption("me", keyTable))