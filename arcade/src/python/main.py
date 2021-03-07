import math
from random import random

import javascript
from browser import window

from .inputs import handle_keys
from .settings import Settings
from .state import State

state = State()
settings = Settings()

game_config = {
    "type": window.Phaser.AUTO,
    "width": window.innerWidth,
    "height": window.innerHeight,
    "scene": {
        "preload": preload,
        "create": create,
        "update": update,
    },
    "physics": {
        "default": "arcade",
    },
}


def preload():
    this = javascript.this()
    this.load.setBaseURL("./assets")
    this.load.image("ship", "ship.svg")
    this.load.image("ufo", "026-ufo.svg")


def create(*args):
    create_ship()
    create_ufo()
    create_score_counter()

    this = javascript.this()
    this.physics.add.collider(state.ship, state.ufo, game_over)


def update(*args):
    ship = state.ship
    ufo = state.ufo

    handle_keys()

    ship.rotation = ship.body.angle + math.pi / 2

    ufo.setAccelerationX(
        (ship.x - ufo.x) * settings.enemy_acceleration * random()
    )
    ufo.setAccelerationY(
        (ship.y - ufo.y) * settings.enemy_acceleration * random()
    )


def game_over(*args):
    print(state.score)


if __name__ == "__main__":
    game = window.Phaser.Game.new(game_config)
