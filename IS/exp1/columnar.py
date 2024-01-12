def orderOfCol(keyword):
    unique_letters = sorted(set(keyword))
    order_dict = {letter: str(index) for index, letter in enumerate(unique_letters)}
    column_order = ''.join(order_dict[letter] for letter in keyword)
    column_order = [int(char) for char in [*column_order]]
    column_index_order = []
    for index, col in enumerate(column_order):
        column_index_order.append((col, index))

    return sorted(column_index_order, key= lambda column: column[0])

def columnarEncrypt(plaintext, key):
    columns = len(key)
    x = len(plaintext)%columns
    for i in range(0, 4 - x):
        plaintext += "_"
    rows = int(len(plaintext)/columns)
    encryptionTable = [["" for i in range(columns)] for i in range(rows)]
    text_index = 0
    for i in range(rows):
        for j in range(columns):
            encryptionTable[i][j] = plaintext[text_index]
            text_index += 1
    
    ciphertext = ""
    col_order = orderOfCol(key)
    for col in col_order:
        for i in range(len(encryptionTable)):
            ciphertext += encryptionTable[i][col[1]]
    return ciphertext



plaintext = input("Plain Text: ")
plaintext = plaintext.replace(" ", "_")

key = input("Key: ")
ciphertext = columnarEncrypt(plaintext, key)
print("Cipher Text: " + ciphertext)
