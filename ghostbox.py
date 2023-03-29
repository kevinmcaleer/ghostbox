# GhostBox.py
# Kevin McAleer
# October 2022

# Note this project uses the batteries included MicroPython firmware from Pimoroni,
# which can be found here:
# www.github.com/pimoroni/pimoroni-pico

from random import choice, randrange
from time import sleep

import binascii
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2
import jpegdec
from time import sleep
from pimoroni import RGBLED, Button
import gc
#from gui import Listbox, hsv_to_rgb
import math
import machine

gc.collect()

display = PicoGraphics(DISPLAY_PICO_DISPLAY_2, rotate=0)
WIDTH, HEIGHT = display.get_bounds()
SCALE = 1
SPACING = 1
WORD_WRAP = WIDTH -2

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

led = RGBLED(6, 7, 8)
led.set_rgb(0, 0, 0)

print(f'Width {WIDTH}, Height {HEIGHT}')

white = {'red': 255, 'green': 255, 'blue': 255}
black = {'red': 0, 'green': 0, 'blue': 0}

def draw_jpg(display, filename):
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file(filename)

    WIDTH, HEIGHT = display.get_bounds()
    display.set_clip(0, 0, WIDTH, HEIGHT)

    # Decode the JPEG
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)
    display.remove_clip()
    display.update()

GHOST_WORDS = "ghostwords.txt"
BACKGROUND = "ghostbox.jpg"
MIN_WAIT = 1
MAX_WAIT = 10

def load_ghost_words():
    with open(GHOST_WORDS, "r") as f:
        return f.read().splitlines()

# load the ghost words
words = load_ghost_words()
white_pen = display.create_pen(white['red'],white['green'],white['blue'])
black_pen = display.create_pen(black['red'],black['green'],black['blue'])

display.set_font('gothic')

while True:
    # wait a random amount of time
    wait = randrange(MIN_WAIT, MAX_WAIT)
    #print(f'waiting for {wait} seconds')
    sleep(wait)
    display.set_pen(black_pen)
    display.clear()
    draw_jpg(display,BACKGROUND)
    display.update()
    
    # pick a random word
    word = choice(words)
    print(word)
    display.set_pen(white_pen)
    length = display.measure_text(word,SCALE,SPACING)
    mid_point = WIDTH //2
    x = mid_point - ( length // 2)
    print(f'length: {length}, mid_point: {mid_point}, x: {x}')
    y = 100
    display.text(word, x,y,WORD_WRAP,SCALE)
    display.update()