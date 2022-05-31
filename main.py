basic.show_string("Good morning!")
basic.show_icon(IconNames.HEART)      
basic.show_leds("""
# # # # .
# . . # .
# # # . .
# . . # .
# . .  #
""")
def on_button_pressed_a():
    basic.show_string("Birthday Year!")
basic.show_number(2005)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_a2():
    basic.show_string("My Age")
    basic.show_number(24)
input.on_button_pressed(Button.B, on_button_pressed_a2)