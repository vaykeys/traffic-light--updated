# Turn off the green light (P2)

def on_forever():
    # Define a function called on_forever
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.show_string("Stop!")
    # Turn on the red light (P0)
    basic.pause(5000)
    # Pause for 5 seconds
    basic.pause(5000)
    # Pause for an additional 5 seconds
    pins.digital_write_pin(DigitalPin.P0, 0)
    # Turn off the red light (P0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.show_string("Get Ready!")
    # Turn on the amber light (P1)
    basic.pause(5000)
    basic.pause(5000)
    pins.digital_write_pin(DigitalPin.P1, 0)
    # Turn off the amber light (P1)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.show_string("Move!")
    # Turn on the green light (P2)
    basic.pause(5000)
    basic.pause(5000)
    pins.digital_write_pin(DigitalPin.P2, 0)
basic.forever(on_forever)
