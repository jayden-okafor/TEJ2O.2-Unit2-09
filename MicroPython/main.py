"""
Created by: Jayden
Created on: Mar 2026
This program chooses between rock, paper or scissors and tracks score.
"""

from microbit import *
import random

# Variables (Starting at 0 so the math works)
random_number = 0
score = 0

display.show(Image.HAPPY)

while True:

    # 1. THE SHAKE
    if accelerometer.was_gesture("shake"):
        random_number = random.randint(0, 2)
        display.clear()

        if random_number == 0:
            display.show(Image.SQUARE_SMALL)

        if random_number == 1:
            display.show(Image.SQUARE)

        if random_number == 2:
            display.show(Image("99009:" "99090:" "00900:" "99090:" "99009"))

        sleep(1000)
        display.show(Image.HAPPY)

    # 2. BUTTON A (Add to Score)
    if button_a.was_pressed():
        score = score + 1
        display.show(Image.YES)
        sleep(500)
        display.show(Image.HAPPY)

    # 3. BUTTON B (Check Score)
    if button_b.was_pressed():
        # You have to use str() to show numbers in Python
        display.scroll(str(score))
        display.show(Image.HAPPY)
