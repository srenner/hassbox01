# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.

Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy

Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel
import digitalio
import wifi
import secrets
#from adafruit_httpserver import HTTPServer, HTTPResponse

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
x = 0

ssid = secrets.ssid
print("Connecting to", ssid)
wifi.radio.connect(ssid, secrets.password)
print("Connected to", ssid)
print(f"Listening on http://{wifi.radio.ipv4_address}")

while True:
    pixels.fill(white)
    time.sleep(0.5)
    pixels.fill(red)
    time.sleep(0.5)
    pixels.fill(green)
    time.sleep(0.5)
    x = x + 1
    print(x)

print("Goodbye")
