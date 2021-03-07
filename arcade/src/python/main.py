import javascript
from browser import window

Phaser = window.Phaser


class Game(object):
    def __init__(self):
        self.game = window.Phaser.Game.new(
            {
                "type": Phaser.AUTO,
                "scene": {
                    "preload": self.preload,
                    "create": self.create,
                },
            }
        )

    def preload(self, *args):
        this = javascript.this()
        this.load.setBaseURL("./assets")
        this.load.image("ship", "ship.svg")
        this.load.image("ufo", "026-ufo.svg")
        this.load.image("sky", "sky.svg")

    def create(self, *args):
        this = javascript.this()
        this.add.image(400, 300, "ship")


if __name__ == "__main__":
    GAME = Game()
