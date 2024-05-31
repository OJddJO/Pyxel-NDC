import pyxel

class Player:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.vy = 0
        self.frame = 0
        self.tick = 0
        self.mirror = 1
        self.jumpTime = 0
        self.isJumping = False
        self.floor = False

    def move(self) -> None:
        self.x += pyxel.btn(pyxel.KEY_RIGHT) - pyxel.btn(pyxel.KEY_LEFT)

    def jump(self) -> None:
        if (pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_SPACE)) and self.floor:
            self.floor = False
            self.isJumping = True
            self.vy = -0.5
        if self.isJumping:
            self.vy -= 0.1
            self.y += self.vy
            self.jumpTime += 1
            if self.jumpTime > 17:
                self.isJumping = False
                self.jumpTime = 0
    
    def gravity(self) -> None:
        if not self.isJumping:
            self.floor = False
            if self.y >= 120-16:
                self.y = 120-16
                self.floor = True
        if not self.isJumping and not self.floor:
            self.vy += 0.1
            if self.y + self.vy > 120-16:
                self.y = 120-16
                self.vy = 0
            self.y += self.vy

    def animate(self, v:int, maxFrame:int, fps:int, mirror:int=1) -> None:
        """v: row of the sprite sheet, maxFrame: number of frames in the row from 0, fps: frames per second"""
        self.frame = self.frame + 1 if self.tick%fps == 0 else self.frame
        if self.frame > maxFrame:
            self.frame = 0
        pyxel.blt(self.x, self.y, 0, self.frame*16, v*16, mirror*16, 16, 8)

    def draw(self) -> None:
        if (not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_RIGHT)):
            self.animate(3, 1, 30, self.mirror)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mirror = 1
            self.animate(1, 2, 10)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mirror = -1
            self.animate(1, 2, 10, -1)
        self.tick = self.tick + 1 if self.tick < 59 else 0

    def update(self) -> None:
        self.gravity()
        self.jump()
        self.move()
