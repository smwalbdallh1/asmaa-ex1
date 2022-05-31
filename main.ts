basic.showString("Good morning!")
basic.showIcon(IconNames.Heart)
basic.showLeds(`
# # # # .
# . . # .
# # # . .
# . . # .
# . .  #
`)
basic.showNumber(2005)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Birthday Year!")
})
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    basic.showString("My Age")
    basic.showNumber(24)
})
