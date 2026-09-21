import machine
import neopixel
import time

# MicroPython Code for Lamp Base Replacement
# NeoPixel Data Pin
PIXEL_PIN = 5
# Number of NeoPixels in Ring or Strip
NUM_PIXELS = 16

# Setup pin and NeoPixel object
pin = machine.Pin(PIXEL_PIN, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_PIXELS)

# Example color vars
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)
CYAN=(0, 255, 255)
PURPLE=(255, 0, 255)
WHITE=(255, 255, 255)
ORANGE=(255, 127, 0)
AMBER=(255, 191, 51)
OFF=(0, 0, 0)


def set_color(color=WHITE):
    """
    set_color(color)
    color: Can be a predefined var or a tuple with the color code
    """
    np.fill(color)
    np.write()


# Main loop for cycling colors every 10 seconds. For a Single color,
# remove and just set_color(TheColorValue)
while True:
    
    for x in [RED, ORANGE, AMBER, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]:
        set_color(x)
        time.sleep(10)
    