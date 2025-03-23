input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    Switch = 0
})
input.onGesture(Gesture.ScreenDown, function () {
    Switch = 0
})
// Zauberin bietet eine frewillige Person nach, ob sie auf A drücken kann. Da Switch = 0, dann wird A gezeigt. Dann bietet nach, B zu drücken. Also B wird angezeigt.
input.onButtonPressed(Button.A, function () {
    if (Switch != 1) {
        basic.showString("A")
    } else {
        basic.showString("B")
    }
})
input.onButtonPressed(Button.B, function () {
    if (Switch != 1) {
        basic.showString("B")
    } else {
        basic.showString("A")
    }
})
let Switch = 0
Switch = 0
// Zauberin nähert Zauberstack und sagt ABRA CADABRA. Switch wird somit auf 1 gesetzt. Dann nachgefragt wird die frewillige Person ob sie wieder A und B drücken kann. WOW!
basic.forever(function () {
    if (input.magneticForce(Dimension.Strength) > 300) {
        Switch = 1
    }
})
