import javascript
from browser import window
from menu import Menu
from seeker import Seeker
from rest import get_top_scores, post_score


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
    name = "Joel"
    get_top_scores(lambda x: print(x))
    post_score(name, score, lambda x: print(x))


if __name__ == "__main__":
    start_game()
