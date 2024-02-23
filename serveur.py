#
#   
#

import time
import zmq
from rpi_ws281x import *

context = zmq.Context()
 
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # wait for next request from client
    message = socket.recv()
    print()



SORTIE_LEDS = [
      [1, 2, 3],          # sortie A0 associees aux leds 1, 2, 3
      [4],                # sortie A#0 associees aux led 4
      [5, 6, 7],          # sortie B0 associees aux leds 5, 6, 7
      [8, 9],             # sortie C1 associees aux leds 8, 9
      [10],               # sortie C#1 associees aux led 10
      [11, 12, 13],       # sortie D1 associees aux leds 11,12,13
      [14],               # sortie D#1 associees aux led 14
      [15, 16, 17],       # sortie E1 associees aux leds 15,16,17
      [18, 19],           # sortie F1 associees aux leds 18,19
      [20],               # sortie F#1 associees aux led 20
      [21, 22, 23],       # sortie G1 associees aux leds 21,22,23
      [24],               # sortie G#1 associees aux led 24
      [25, 26, 27],       # sortie A1 associees aux leds 25,26,27
      [28],               # sortie A#1 associees aux led 28
      [29, 30],           # sortie B1 associees aux leds 29, 30
      [31, 32, 33],       # sortie C2 associees aux leds 31, 32, 33
      [34],               # sortie C#2 associees aux led 34
      [35, 36, 37],       # sortie D2 associees aux leds 35, 36, 37
      [38],               # sortie D#2 associees aux led 38
      [39, 40, 41],       # sortie E2 associees aux leds 39, 40, 41
      [42, 43],           # sortie F2 associees aux leds 42, 43
      [44],               # sortie F#2 associees aux led 44
      [45, 46, 47],       # sortie G2 associees aux leds 45, 46, 47
      [48],               # sortie G#2 associees aux led 48
      [49, 50, 51],       # sortie A2 associees aux leds 49, 50, 51
      [52],               # sortie A#2 associees aux led 52
      [53, 54],           # sortie B2 associees aux leds 53, 54
      [55, 56],           # sortie C3 associees aux leds 55, 56
      [57, 58],           # sortie C#3 associees aux leds 57, 58
      [59, 60, 61],       # sortie D3 associees aux leds 59, 60, 61
      [62],               # sortie D#3 associees aux led 62
      [63, 64],           # sortie E3 associees aux leds 63, 64
      [65, 66, 67],       # sortie F3 associees aux leds 65, 66, 67
      [68],               # sortie F#3 associees aux leds 68
      [69, 70],           # sortie G3 associees aux leds 69, 70
      [71],               # sortie G#3 associees aux led 71
      [72, 73, 74],       # sortie A3 associees aux leds 72, 73, 74
      [75],               # sortie A#3 associees aux led 75
      [76, 77, 78],       # sortie B3 associees aux leds 76, 77, 78
      [79, 80],           # sortie C4 associees aux leds 79, 80
      [81, 82],           # sortie C#4 associees aux leds,81, 82
      [83, 84, 85],       # sortie D4 associees aux leds 83, 84, 85
      [86],               # sortie D#4 associees aux led 86
      [87, 88],           # sortie E4 associees aux leds 87, 88
      [89, 90],           # sortie F4 associees aux leds 89, 90
      [91, 92],           # sortie F#4 associees aux leds 91, 92
      [93, 94],           # sortie G4 associees aux leds 93, 94
      [95, 96],           # sortie G#4 associees aux leds 95, 96
      [97, 98],           # sortie A4 associees aux leds 97, 98
      [99],               # sortie A#4 associees aux led 99
      [100, 101, 102],    # sortie B4 associees aux leds 100, 101, 102
      [103, 104],         # sortie C5 associees aux leds 103, 104
      [105],              # sortie C#5 associees aux led 105
      [106, 107, 108],    # sortie D5 associees aux leds 106, 107, 108
      [109],              # sortie D#5 associees aux led 109
      [110, 111, 112],    # sortie E5 associees aux leds 110, 111, 112
      [113, 114],         # sortie F5 associees aux leds 113, 114
      [115],              # sortie F#5 associees aux led 115
      [116, 117, 118],    # sortie G5 associees aux leds 116, 117, 118
      [119],              # sortie G#5 associees aux led 119
      [120, 121, 122],    # sortie A5 associees aux leds 120, 121, 122
      [123],              # sortie A#5 associees aux led 123
      [124, 125],         # sortie B5 associees aux leds 124, 125
      [126, 127, 128],    # sortie C6 associees aux leds 126, 127, 128
      [129],              # sortie C#6 associees aux led 129
      [130, 131, 132],    # sortie D6 associees aux leds 130, 131, 132
      [133],              # sortie D#6 associees aux led 133
      [134, 135],         # sortie E6 associees aux leds 134, 135
      [136, 137, 138],    # sortie F6 associees aux leds 136, 137, 138
      [139],              # sortie F#6 associees aux led 139
      [140, 141],         # sortie G6 associees aux leds 140, 141
      [142, 143],         # sortie G#6 associees aux leds 142, 143
      [144, 145],         # sortie A6 associees aux leds 144, 145
      [146],              # sortie A#6 associees aux led 146
      [147, 148],         # sortie B6 associees aux leds 147, 148
      [149, 150, 151],    # sortie C7 associees aux leds 149, 150, 151
      [152],              # sortie C#7 associees aux led 152
      [153, 154, 155],    # sortie D7 associees aux leds 153, 154, 155
      [156],              # sortie D#7 associees aux led 156
      [157, 158, 159],    # sortie E7 associees aux leds 157, 158, 159
      [160, 161],         # sortie F7 associees aux leds 160, 161
      [162],              # sortie F#7 associees aux led 162
      [163, 164, 165],    # sortie G7 associees aux leds 163, 164, 165
      [166],              # sortie G#7 associees aux led 166
      [167, 168, 169],    # sortie A7 associees aux leds 167, 168, 169
]

curMsg = 0


while True:
    #  Wait for next request from client
    sleep(1)
    socket.send_pyobj({curMsg:SORTIE_LEDS})
    print("Received request: %s" % message)
 
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")