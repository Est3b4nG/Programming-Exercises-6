"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Extend the example01.py to vertically move a text while its color 
changes. Once it reaches the
bottom of the screen it appears again at the beginning"""

import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.text(2, 2, "Learning is fun", 2)
    pyxel.text(2, 15, "Changing color every frame", pyxel.frame_count % 16)
    x = pyxel.frame_count % pyxel.width
    pyxel.text(x, 30, "Moving text", 3)
    y= pyxel.frame_count % pyxel.height
    pyxel.text(50,y, "Vertically Moving Text", pyxel.frame_count % 16)

WIDTH = 200
HEIGHT = 200
CAPTION = "This is the first pyxel example"
pyxel.init(WIDTH, HEIGHT, title=CAPTION)
pyxel.run(update, draw)
