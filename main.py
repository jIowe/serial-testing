def on_button_pressed_a():
    serial.write_line("Button A Pressed")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    serial.write_line("Button B Pressed")
input.on_button_pressed(Button.B, on_button_pressed_b)

serial.write_line("successfully downloaded code")
