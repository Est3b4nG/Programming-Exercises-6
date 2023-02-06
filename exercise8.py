"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Modify the example02.py so any of its figures moves in a diagonal direction until it disappears
from the screen (it stops moving then)"""

import pyxel

def move():


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(1)
    pyxel.line(0,0, 10, 10, 2)
    pyxel.rectb(30, 50, 20, 10, 5)
    pyxel.circ(50, 80, 10, 6)
    pyxel.circb(100, 30, 15, 7)
    pyxel.pset(120, 100, 8)
    x = pyxel.frame_count % pyxel.width
    y = pyxel.frame_count % pyxel.height
    if pyxel.frame_count<pyxel.width:
        pyxel.rect(x, y, 10, 10, 4)
    if pyxel.frame_count==pyxel.width:
        pyxel.rect(151, 151, 10, 10, 4)


Width=150
Height=150
CAPTION = "This is an example of drawing figures in pyxel"

pyxel.init(150,160,title=CAPTION)
pyxel.run(update , draw)