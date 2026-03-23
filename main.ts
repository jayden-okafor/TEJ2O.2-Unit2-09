/* Copyright (c) 2026 MTHS All rights reserved
 *
 * Created by: Jayden
 * Created on: Mar 2026
 * This program chooses between rock, paper or scissors when you shake the microbit. 
 */

// variables
let randomNumber: number = null
let score: number = null

basic.clearScreen()
basic.showIcon(IconNames.Happy)

input.onGesture(Gesture.Shake, function () {
    // generate random number between 0 and 2
    randomNumber = randint(0, 2)
    basic.clearScreen()

    // if the randomised number is 0 then show rock
    if (randomNumber == 0) {
        basic.showIcon(IconNames.SmallSquare)
        basic.pause(3000)
        basic.showIcon(IconNames.Happy)
    }

    // if the randomised number is 1 then show paper
    if (randomNumber == 1) {
        basic.showIcon(IconNames.Square)
        basic.pause(3000)
        basic.showIcon(IconNames.Happy)
    }

    // if the randomised number is 2 then show scissors
    if (randomNumber == 2) {
        basic.showIcon(IconNames.Scissors)
        basic.pause(3000)
        basic.showIcon(IconNames.Happy)
    }

})

// when the "a" button is pressed
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()

    // add 1 to the current score value
    score += 1
    basic.showIcon(IconNames.Yes)

    // wait for 1 second
    basic.pause(1000)
    basic.showIcon(IconNames.Happy)
})

// when the "b" button is pressed
input.onButtonPressed(Button.B, function () {
    // clear clearScreen
    basic.clearScreen()

    // show the score
    basic.showString("score:" + score.toString())
    basic.showIcon(IconNames.Happy)
})
