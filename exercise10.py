"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Draw or import two png files in the image bank and move one of them automatically and the
other one using the keyboard"""

import pyxel

position=[10,10]

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
    return x,y

def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])

def draw():
    pyxel.cls(1)
    pyxel.blt(position[0], position[1], 0, 0, 0 , 16, 16)
    x = pyxel.frame_count % pyxel.width
    y = pyxel.frame_count % pyxel.height
    pyxel.blt(x, y, 1, 17, 0, 16, 16)


Width= 150
Height=150
Caption="Exercise 10"

pyxel.init(Width, Height, title=Caption)

pyxel.run(update,draw)

