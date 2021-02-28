def on_button_pressed_a():
    # close the claw
    Servo.servo(0, 105)
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . # . # .
        . # . # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # close the claw
    Servo.servo(0, 195)
    basic.show_leds("""
        . . # . .
        . . # . .
        . # . # .
        # . . . #
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

# initially open the claw
Servo.servo(0, 195)
basic.show_leds("""
    . # . . .
    . # # . .
    . # # # .
    . # # . .
    . # . . .
    """)

def on_forever():
    pass
basic.forever(on_forever)

