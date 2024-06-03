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
        self.floorTime = 0
        #camera
        self.cx = self.x-120
        self.cy = self.y-120

    def move(self) -> None:
        if not self.collision("left"):
            self.x -= pyxel.btn(pyxel.KEY_LEFT)
        if not self.collision("right"):
            self.x += pyxel.btn(pyxel.KEY_RIGHT)
        self.mirror = 1 if pyxel.btn(pyxel.KEY_RIGHT) else -1 if pyxel.btn(pyxel.KEY_LEFT) else self.mirror

    def jump(self) -> None:
        if (pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_SPACE)) and self.floor:
            self.floor = False
            self.floorTime = 0
            self.isJumping = True
            self.vy = -5
        if self.isJumping:
            self.vy += 0.2
            for dy in range(int(abs(self.vy))):
                if self.collision("up", dy):
                    self.vy = 0
                    self.y += dy
                    break
            self.y += self.vy
            self.jumpTime += 1
            if self.jumpTime > 15:
                self.isJumping = False
                self.jumpTime = 0

    def goDown(self) -> None:
        if pyxel.btn(pyxel.KEY_DOWN) and self.floor:
            for i in range(12):
                if pyxel.pget(self.x+2+i-self.cx, self.y+16-self.cy) != 0:
                    self.y += 1
                    self.floor = False
                    self.floorTime = 0
                    self.vy = 2

    def collision(self, side:str, dy:int=0) -> bool:
        match side:
            case "left":
                for i in range(16):
                    if pyxel.pget(self.x+1-self.cx, self.y+i+dy-self.cy) == 0:
                        return True
            case "right":
                for i in range(16):
                    if pyxel.pget(self.x+15-self.cx, self.y+i+dy-self.cy) == 0:
                        return True
            case "up":
                for i in range(12):
                    if pyxel.pget(self.x+2+i-self.cx, self.y-1-dy-self.cy) == 0:
                        return True
            case "down":
                for i in range(12):
                    if pyxel.pget(self.x+2+i-self.cx, self.y+16+dy-self.cy) in [0, 4]:
                        return True
        return False
    
    def gravity(self) -> None:
        if not self.isJumping:
            self.floor = False
            if self.collision("down"):
                self.vy = 0
                self.floor = True
                self.floorTime += 1
        if not self.isJumping and not self.floor:
            self.vy += 0.2
            for dy in range(int(self.vy)):
                if self.collision("down", dy):
                    self.vy = 0
                    self.y += dy-1
                    break
            self.y += self.vy if self.vy < 10 else 10

    def animate(self, v:int, maxFrame:int, fps:int, mirror:int=1) -> None:
        """v: row of the sprite sheet, maxFrame: number of frames in the row from 0, fps: frames per second"""
        self.frame = self.frame + 1 if self.tick%fps == 0 else self.frame
        if self.frame > maxFrame:
            self.frame = 0
        pyxel.blt(self.x, self.y, 0, self.frame*16, v*16, mirror*16, 16, 8)

    def draw(self) -> None:
        if not self.isJumping and self.floor:
            if self.floorTime < 15:
                pyxel.blt(self.x, self.y, 0, 64, 32, self.mirror*16, 16, 8)
                self.tick = 0
            else:
                if (not pyxel.btn(pyxel.KEY_RIGHT) and not pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_LEFT) and pyxel.btn(pyxel.KEY_RIGHT)):
                    self.animate(3, 1, 30, self.mirror)
                elif pyxel.btn(pyxel.KEY_RIGHT):
                    self.animate(1, 2, 10)
                elif pyxel.btn(pyxel.KEY_LEFT):
                    self.animate(1, 2, 10, -1)
        elif self.isJumping:
            if self.jumpTime < 5:
                pyxel.blt(self.x, self.y, 0, 16, 32, self.mirror*16, 16, 8)
            else:
                pyxel.blt(self.x, self.y, 0, 32, 32, self.mirror*16, 16, 8)
        elif not self.floor:
            pyxel.blt(self.x, self.y, 0, 48, 32, self.mirror*16, 16, 8)
        self.tick = self.tick + 1 if self.tick < 59 else 0

    def update(self) -> None:
        self.jump()
        self.move()
        self.goDown()
        self.gravity()
        self.x, self.y = int(self.x), int(self.y)
        self.cx, self.cy = self.x-120, self.y-120
        pyxel.camera(self.cx, self.cy)