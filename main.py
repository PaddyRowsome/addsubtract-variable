_var = 0

def on_forever():
    global _var
    if input.button_is_pressed(Button.A):
        _var += 1
        basic.show_string("" + str((_var)))
    elif input.button_is_pressed(Button.B):
        _var += -1
        basic.show_string("" + str((_var)))
basic.forever(on_forever)
