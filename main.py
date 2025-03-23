def on_logo_pressed():
    global Switch
    Switch = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_screen_down():
    global Switch
    Switch = 0
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

# Zauberin bietet eine frewillige Person nach, ob sie auf A drücken kann. Da Switch = 0, dann wird A gezeigt. Dann bietet nach, B zu drücken. Also B wird angezeigt.

def on_button_pressed_a():
    if Switch != 1:
        basic.show_string("A")
    else:
        basic.show_string("B")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if Switch != 1:
        basic.show_string("B")
    else:
        basic.show_string("A")
input.on_button_pressed(Button.B, on_button_pressed_b)

Switch = 0
Switch = 0
# Zauberin nähert Zauberstack und sagt ABRA CADABRA. Switch wird somit auf 1 gesetzt. Dann nachgefragt wird die frewillige Person ob sie wieder A und B drücken kann. WOW!

def on_forever():
    global Switch
    if input.magnetic_force(Dimension.STRENGTH) > 300:
        Switch = 1
basic.forever(on_forever)
