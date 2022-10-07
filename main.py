strip = neopixel.create(DigitalPin.P0, 32, NeoPixelMode.RGB)
strip.set_brightness(30)

def on_forever():
    strip.show_rainbow(1, 360)
    strip.show()
    while True:
        strip.rotate(1)
        strip.show()
        basic.pause(100)
basic.forever(on_forever)
