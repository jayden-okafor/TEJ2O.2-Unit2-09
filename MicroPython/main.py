"""
Created by: Jayden
Created on: Mar 2026
This program chooses between rock, paper or scissors and tracks score.
"""

from microbit import *
import random

# variables
random_number = 0
score = 0

# clear screen
display.clear()
display.show(Image.HAPPY)

while True:
    if accelerometer.was_gesture("shake"):
        # generate random number between 0 and 2
        random_number = random.randint(0, 2)
        display.clear()

        # if the randomised number is 0 then show rock
        if random_number == 0:
            display.show(Image.SQUARE_SMALL)
            sleep(3000)

        # if the randomised number is 1 then show paper
        if random_number == 1:
            display.show(Image.SQUARE)
            sleep(3000)

        # if the randomised number is 2 then show scissors
        if random_number == 2:
            display.show(Image("99009:" "99090:" "00900:" "99090:" "99009"))
            sleep(3000)

    # when the "a" button is pressed
    if button_a.was_pressed():

        # add 1 to the current score value
        score += 1

        # show checkmark
        display.show(Image.YES)

        # wait for 5 seconds
        sleep(500)

        # show happy face
        display.show(Image.HAPPY)

    # when the "b" button is pressed
    if button_b.was_pressed():
        # show the score
        display.scroll(str(score))
        display.show(Image.HAPPY)
