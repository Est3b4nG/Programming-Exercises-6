"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Modify the example03.py so the circle cannot move outside the screen (no part of it can be
outside the screen)
"""

import pyxel

position =[10, 10]

def move(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT) and x==140:
        x=x
    elif pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT) and x==10:
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
    elif pyxel.btn(pyxel.KEY_UP) and y==10:
        y = y
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN) and y==140:
        y = y
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1

    return x, y


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])

def draw():
    pyxel.cls(0)
    pyxel.circ(position[0], position[1], 10, 10)



Width=150
Height=150
Caption="Exercise 9"

pyxel.init(Width,Height,title=Caption)

pyxel.run(update, draw)
