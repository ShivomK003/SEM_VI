

def orderOfCol(keyword):
    unique_letters = sorted(set(keyword))
    order_dict = {letter: str(index) for index, letter in enumerate(unique_letters)}
    column_order = ''.join(order_dict[letter] for letter in keyword)
    column_order = [int(char) for char in [*column_order]]
    column_index_order = []
    for index, col in enumerate(column_order):
        column_index_order.append((col, index))
    return sorted(column_index_order, key= lambda column: column[0])


def columnarDecrypt(ciphertext, key):
    columns = len(key)
    rows = int(len(ciphertext)/len(key))
    decryptionTable = [["" for i in range(columns)] for i in range(rows)]
    col_substring = [ciphertext[i:i+len(key)] for i in range(0, len(ciphertext), len(key))]
    col_order = orderOfCol(key)
    for col in col_order: # 1
        string_index = 0
        for i in range(rows):
            decryptionTable[i][col[1]] = col_substring[col[0]][string_index]
            string_index+=1
    plaintext = ""
    for i in range(rows):
        for j in range(columns):
            plaintext += decryptionTable[i][j]
    plaintext = plaintext.replace("_", " ")
    return(plaintext)


ciphertext = input("Cipher Text: ") 
key = input("Key: ")
plaintext = columnarDecrypt(ciphertext, key)
print("Plain Text: " + plaintext)

