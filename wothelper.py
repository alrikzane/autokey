import pygetwindow as gw
from pynput.mouse import Button, Controller
import time



mouse = Controller()

#get list of all windows, which include "езым" in their name
win = gw.getAllWindows()
wot_objects = []
for x in win:
    if 'езым' in x.title:
        x.resizeTo(500,500) 
        wot_objects.append(x)



for x in wot_objects:
    mouse.position = (x.left+250, x.bottom-200)
    x.activate()
    time.sleep(0.05)
    mouse.press(Button.left)
    mouse.move(0,50)
    mouse.release(Button.left)

    