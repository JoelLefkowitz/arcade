from browser import window
from dom import show_results
from menu import Menu
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
    top_scores = get_top_scores()
    show_results(score, top_scores)


if __name__ == "__main__":
    # start_game()
    show_results(10, [1, 2, 3])
