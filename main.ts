let strip = neopixel.create(DigitalPin.P0, 32, NeoPixelMode.RGB)
strip.setBrightness(30)
basic.forever(function () {
    strip.showRainbow(1, 360)
    strip.show()
    while (true) {
        strip.rotate(1)
        strip.show()
        basic.pause(100)
    }
})
