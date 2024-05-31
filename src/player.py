import pyxel
from math import sqrt

class Player:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.frame = 0
        self.tick = 0
        self.mirror = 1

    def move(self) -> None:
        self.x += pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT)

    def animate(self, v:int, maxFrame:int, fps:int, mirror:int=1) -> None:
        """v: row of the sprite sheet, maxFrame: number of frames in the row from 0, fps: frames per second"""
        self.frame = self.frame + 1 if self.tick%fps == 0 else self.frame
        if self.frame > maxFrame:
            self.frame = 0
        pyxel.blt(self.x, self.y, 0, self.frame*16, v*16, mirror*16, 16, 8)

    def draw(self) -> None:
        if (not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_RIGHT)):
            self.animate(1, 1, 30, self.mirror)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mirror = 1
            self.animate(0, 2, 10)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mirror = -1
            self.animate(0, 2, 10, -1)
        self.tick = self.tick + 1 if self.tick < 59 else 0

    def update(self) -> None:
        self.move()
