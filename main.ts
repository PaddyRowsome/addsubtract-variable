let _var = 0
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        _var += 1
        basic.showString("" + (_var))
    } else if (input.buttonIsPressed(Button.B)) {
        _var += -1
        basic.showString("" + (_var))
    }
})
