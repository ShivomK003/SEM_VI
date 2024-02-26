import random
import string

R1 = random.randint(4,9)
captcha = ""

i = 0
while i < R1:
    R3 = ""
    R2 = random.randint(1,9)
    if R2 > 6:
        R3 = str(random.randint(0, 9))
    else:
        R3 = random.choice(string.ascii_uppercase) 
    captcha += R3
    i += 1

print(captcha)