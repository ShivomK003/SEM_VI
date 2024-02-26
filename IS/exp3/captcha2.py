import random
import string
import cv2
import numpy as np

def add_noise(img):
    row , col = img.shape[0], img.shape[1] 
    number_of_pixels = random.randint(300, 10000) 
    for i in range(number_of_pixels): 
         y_coord=random.randint(0, row - 1) 
         x_coord=random.randint(0, col - 1) 
         img[y_coord][x_coord] = 255
    
    number_of_pixels = random.randint(300 , 10000) 
    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1) 
        img[y_coord][x_coord] = 0


def generate_captcha_text():
    R1 = random.randint(4,6)
    captcha = ""
    print(R1)
    i = 0
    while i < R1:
        R3 = ""
        R2 = random.randint(1,9)
        if R2 > 6:
            R3 = str(random.randint(0, 9)) + " "
        else:
            R3 = random.choice(string.ascii_uppercase) + " "
        captcha += R3
        i += 1

    return captcha

def generate_image(text):
    image = cv2.imread("IS\exp3\captcha_bg.jpg")
    image = image[500:900, :]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 4
    font_thickness = 15

    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
    print(text_height, text_width)
    x = (image.shape[1] - text_width) // 2
    y = (image.shape[0] + text_height) // 2

    cv2.putText(image, text, (x, y), font, font_scale, (0, 0, 0), font_thickness)

    add_noise(image)

    cv2.imwrite("output.png", image)



width = 640
height = 640
captcha_text = generate_captcha_text()
generate_image(captcha_text)