import pyxel
import player

class App:
    def __init__(self) -> None:
        pyxel.init(256, 256 , "Title", fps=60, quit_key=pyxel.KEY_NONE)
        pyxel.load("theme2.pyxres")

        self.player = player.Player(0, 80)

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.player.update()

    def draw(self) -> None:
        pyxel.cls(1)
        pyxel.bltm(0, 0, 0, 0, 0, 2048, 2048, 8)
        pyxel.rect(0, 120, 128, 8, 0)
        self.player.draw()

if __name__ == "__main__":
    App()