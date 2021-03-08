import javascript
from browser import window
from base import BaseScene


class Menu(BaseScene):
    key = "Menu"
    button = None

    def preload(self):
        this = javascript.this()
        this.load.setBaseURL("./assets")

    def create(self, *args):
        this = javascript.this()
        self.button = this.add.text(
            window.innerWidth / 2,
            window.innerHeight / 2,
            "Start game!",
            {"fill": "#00FF00"},
        ).setOrigin(0.5)

        self.button.setInteractive()
        self.button.on(
            "pointerdown", lambda *args: this.scene.start("Seeker")
        )

    def update(self, *args):
        pass
