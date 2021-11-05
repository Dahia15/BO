# Add your Python code here. E.g.
from microbit import *
import music

while True:
    if accelerometer.was_gesture('shake'):
        music.play(music.ODE)
    if button_b.was_pressed():
        music.play(music.BLUES) 
