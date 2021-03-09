from browser import window
from menu import Menu
from modal import show_results
from rest import get_top_scores
from seeker import Seeker


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
    get_top_scores(
        callback=lambda top_scores: show_results(score, top_scores)
    )


if __name__ == "__main__":
    start_game()
