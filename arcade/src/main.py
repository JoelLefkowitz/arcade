from browser import window
from scenes.menu import Menu
from scenes.seeker import Seeker


def start_game():
    menu = Menu()
    seeker = Seeker(callback=game_over)

    game = window.Phaser.Game.new(
        {
            "type": window.Phaser.AUTO,
            "width": window.innerWidth,
            "height": window.innerHeight,
            "physics": {
                "default": "arcade",
            },
            "scene": [menu.scene, seeker.scene],
        }
    )


def game_over(score):
    print(score)


if __name__ == "__main__":
    start_game()
