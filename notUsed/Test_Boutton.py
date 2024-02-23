from gpiozero import LED, Button
from time import sleep

#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

from signal import pause
from typing import List
from functools import partial
from rpi_ws281x import *
import argparse
from gpiozero import Button

# LED strip configuration:
LED_COUNT = 169      # Number of LED pixels.
LED_PIN = 10        # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Button pins connection
BTN_PIN_1 = 3
BTN_PIN_2 = 4
BTN_PIN_3 = 5
BTN_PIN_4 = 6
BTN_PIN_5 = 7
BTN_PIN_6 = 8
BTN_PIN_7 = 9
BTN_PIN_8 = 10
BTN_PIN_9 = 11
BTN_PIN_10 = 12
BTN_PIN_11 = 13
BTN_PIN_12 = 14
BTN_PIN_13 = 15
BTN_PIN_14 = 16
BTN_PIN_15 = 17
BTN_PIN_16 = 18
BTN_PIN_17 = 19
BTN_PIN_18 = 20
BTN_PIN_19 = 21
BTN_PIN_20 = 22
BTN_PIN_21 = 23
BTN_PIN_22 = 24
BTN_PIN_23 = 25
BTN_PIN_24 = 26
BTN_PIN_25 = 27
BTN_PIN_26 = 28
BTN_PIN_27 = 29
BTN_PIN_28 = 30
BTN_PIN_29 = 31
BTN_PIN_30 = 32
BTN_PIN_31 = 33
BTN_PIN_32 = 34
BTN_PIN_33 = 35
BTN_PIN_34 = 36
BTN_PIN_35 = 37
BTN_PIN_36 = 38
BTN_PIN_37 = 39
BTN_PIN_38 = 40
BTN_PIN_39 = 41
BTN_PIN_40 = 42
BTN_PIN_41 = 43
BTN_PIN_42 = 44
BTN_PIN_43 = 45
BTN_PIN_44 = 46
BTN_PIN_45 = 47
BTN_PIN_46 = 48
BTN_PIN_47 = 49
BTN_PIN_48 = 50
BTN_PIN_49 = 51
BTN_PIN_50 = 52
BTN_PIN_51 = 53
BTN_PIN_52 = 54
BTN_PIN_53 = 55
BTN_PIN_54 = 56
BTN_PIN_55 = 57
BTN_PIN_56 = 58
BTN_PIN_57 = 59
BTN_PIN_58 = 60
BTN_PIN_59 = 61
BTN_PIN_60 = 62
BTN_PIN_61 = 63
BTN_PIN_62 = 64
BTN_PIN_63 = 65
BTN_PIN_64 = 66
BTN_PIN_65 = 67
BTN_PIN_66 = 68
BTN_PIN_67 = 69
BTN_PIN_68 = 70
BTN_PIN_69 = 71
BTN_PIN_70 = 72
BTN_PIN_71 = 73
BTN_PIN_72 = 74
BTN_PIN_73 = 75
BTN_PIN_74 = 76
BTN_PIN_75 = 77
BTN_PIN_76 = 78
BTN_PIN_77 = 79
BTN_PIN_78 = 80
BTN_PIN_79 = 81
BTN_PIN_80 = 82
BTN_PIN_81 = 83
BTN_PIN_82 = 84
BTN_PIN_83 = 85
BTN_PIN_84 = 86
BTN_PIN_85 = 87


def set_leds(strip: PixelStrip, leds: List[int], color: Color) -> None:
    """Set specific leds from strip to a certain color.

    :param strip: led strip to operat on
    :param leds: list of leds position to set
    :param color: color in which to set the leds
    """
    for i in leds:
        strip.setPixelColor(i, color)


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    # map button press/release to led light up
    btn_list = [
        # (bouton, [list de leds associees])
        (Button(BTN_PIN_1):  [1, 2, 3],
         Button(BTN_PIN_2):  [4, 5],
         Button(BTN_PIN_3):  [6, 7],
         Button(BTN_PIN_4):  [8, 9],
         Button(BTN_PIN_5):  [10, 11],
         Button(BTN_PIN_6):  [12, 13, 14],
         Button(BTN_PIN_7):  [15],
         Button(BTN_PIN_8):  [16, 17],
         Button(BTN_PIN_9):  [18, 19],
         Button(BTN_PIN_10): [20],
         Button(BTN_PIN_11): [21, 22],
         Button(BTN_PIN_12): [23, 24],
         Button(BTN_PIN_13): [25, 26],
         Button(BTN_PIN_14): [27, 28],
         Button(BTN_PIN_15): [29, 30],
         Button(BTN_PIN_16): [31, 32],
         Button(BTN_PIN_17): [33, 34],
         Button(BTN_PIN_18): [35, 36],
         Button(BTN_PIN_19): [37, 38],
         Button(BTN_PIN_20): [39, 40, 41],
         Button(BTN_PIN_21): [42, 43],
         Button(BTN_PIN_22): [44],
         Button(BTN_PIN_23): [45, 46, 47],
         Button(BTN_PIN_24): [48],
         Button(BTN_PIN_25): [49, 50, 51],
         Button(BTN_PIN_26): [52],
         Button(BTN_PIN_27): [53, 54],
         Button(BTN_PIN_28): [55, 56],
         Button(BTN_PIN_29): [57, 58],
         Button(BTN_PIN_30): [59, 60, 61],
         Button(BTN_PIN_31): [62],
         Button(BTN_PIN_32): [63, 64],
         Button(BTN_PIN_33): [65,66, 67],
         Button(BTN_PIN_34): [68],
         Button(BTN_PIN_35): [69, 70, 71],
         Button(BTN_PIN_36): [72],
         Button(BTN_PIN_37): [73, 74],
         Button(BTN_PIN_38): [75, 76],
         Button(BTN_PIN_39): [77, 78],
         Button(BTN_PIN_40): [79, 80],
         Button(BTN_PIN_41): [81, 82],
         Button(BTN_PIN_42): [83, 84],
         Button(BTN_PIN_43): [85, 86],
         Button(BTN_PIN_44): [87, 88],
         Button(BTN_PIN_45): [89, 90],
         Button(BTN_PIN_46): [91, 92],
         Button(BTN_PIN_47): [93, 94],
         Button(BTN_PIN_48): [95, 96],
         Button(BTN_PIN_49): [97, 98],
         Button(BTN_PIN_50): [99, 100],
         Button(BTN_PIN_51): [101, 102],
         Button(BTN_PIN_52): [103, 104],
         Button(BTN_PIN_53): [105, 106],
         Button(BTN_PIN_54): [107, 108],
         Button(BTN_PIN_55): [109, 110],
         Button(BTN_PIN_56): [111, 112],
         Button(BTN_PIN_57): [113, 114],
         Button(BTN_PIN_58): [115, 116],
         Button(BTN_PIN_59): [117, 118],
         Button(BTN_PIN_60): [119, 120],
         Button(BTN_PIN_61): [121, 122],
         Button(BTN_PIN_62): [123, 124],
         Button(BTN_PIN_63): [125, 126],
         Button(BTN_PIN_64): [127, 128],
         Button(BTN_PIN_65): [129, 130],
         Button(BTN_PIN_66): [131, 132],
         Button(BTN_PIN_67): [133, 134],
         Button(BTN_PIN_68): [135, 136],
         Button(BTN_PIN_69): [137, 138],
         Button(BTN_PIN_70): [139, 140],
         Button(BTN_PIN_71): [141, 142],
         Button(BTN_PIN_72): [143, 144],
         Button(BTN_PIN_73): [145, 146],
         Button(BTN_PIN_74): [147],
         Button(BTN_PIN_75): [148, 149],
         Button(BTN_PIN_76): [150, 151, 152],
         Button(BTN_PIN_77): [153],
         Button(BTN_PIN_78): [154, 155],
         Button(BTN_PIN_79): [156],
         Button(BTN_PIN_80): [157, 158, 159],
         Button(BTN_PIN_81): [160, 161],
         Button(BTN_PIN_82): [162],
         Button(BTN_PIN_83): [163, 164, 165],
         Button(BTN_PIN_84): [166],
         Button(BTN_PIN_85): [167, 168, 169],
        ),
    ]

    for btn, leds in btn_list:
        btn.when_pressed = partial(set_leds, strip, leds, Color(163, 51, 204))
        btn.when_released = partial(set_leds, strip, leds, (0))

    pause()

