import pyxel
import player

class App:
    """Main class for the game."""
    def __init__(self) -> None:
        """Constructor for the App class."""
        pyxel.init(128, 128 , "Title", fps=60, quit_key=pyxel.KEY_NONE)
        pyxel.load("theme2.pyxres")

        self.player = player.Player(80, 60)

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        """Update method for the App class."""
        self.player.update()

    def draw(self) -> None:
        """Draw method for the App class."""
        pyxel.cls(1)
        pyxel.rect(0, 120, 128, 8, 3)
        self.player.draw()

if __name__ == "__main__":
    App()