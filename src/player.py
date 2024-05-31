import pyxel
from math import sqrt

class Player:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self) -> None:
        self.x += pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT)

    def decrease_vel(self) -> None:
        self.vel = 0.5

    def draw(self) -> None:
        pyxel.rect(self.x, self.y, 8, 8, 1)

    def update(self) -> None:
        self.move()
