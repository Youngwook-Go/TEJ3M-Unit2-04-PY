"""
Created by: Youngwook Go
Created on: OCT 2023
Blinks a LED
"""

import time
import board
import digitalio

red = digitalio.DigitalInOut(board.GP0)
green = digitalio.DigitalInOut(board.GP1)
blue = digitalio.DigitalInOut(board.GP3)

red.direction = digitalio.Direction.OUTPUT
green.direction = digitalio.Direction.OUTPUT
blue.direction = digitalio.Direction.OUTPUT

while True:
red.value = True
green.value = False
blue.value = False
print("Red")
time.sleep(1)

red.value = False
green.value = True
blue.value = False
print("Green")
time.sleep(1)

red.value = False
green.value = False
blue.value = True
print("Blue")
time.sleep(1)

red.value = True
green.value = True
blue.value = False
print("Yellow")
time.sleep(1)

red.value = False
green.value = True
blue.value = True
print("Cyan")
time.sleep(1)

red.value = True
green.value = False
blue.value = True
print("Magenta")
time.sleep(1)

red.value = True
green.value = True
blue.value = True
print("White")
time.sleep(1)