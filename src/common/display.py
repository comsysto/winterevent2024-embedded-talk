import ssd1306

from utime import sleep, sleep_ms
from machine import Pin, I2C


# defaults
# - Esp8266Display
WIDTH = 128
HEIGHT = 64

SDA_PIN = 12
SCL_PIN = 14

EMPTY_SCREEN_COLOUR = 0
TEXT_COLOUR = 1


class Esp8266Display:
    _width: int
    _height: int
    _display: ssd1306.SSD1306_I2C

    def __init__(self, width: int = WIDTH, height: int = HEIGHT):
        self._width = width
        self._height = height
        i2c = I2C(sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=400000)
        self._display = ssd1306.SSD1306_I2C(width, height, i2c)
        self.reset()

    def reset(self):
        self._display.fill(EMPTY_SCREEN_COLOUR)
        self._display.show()

    def on(self):
        self._display.poweron()

    def off(self):
        self._display.poweroff()

    def message(self,
                message: str,
                row: int = 0,
                reset_before: bool = True,
                reset_after: bool = True,
                duration_s: float = None):
        if reset_before:
            self.reset()

        self._display.text(message, 0, row, TEXT_COLOUR)
        self._display.show()

        if duration_s:
            sleep(duration_s)

        if not duration_s and reset_after:
            self.reset()
