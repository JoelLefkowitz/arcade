from random import random

import javascript

from .main import settings, state


def create_ship():
    this = javascript.this()
    ship = this.physics.add.sprite(
        window.innerWidth / 2, window.innerHeight - 200, "ship"
    )

    ship.displayHeight = 100
    ship.displayWidth = 100

    ship.enableBody = True
    ship.body.collideWorldBounds = True
    ship.body.maxSpeed = settings.max_speed

    ship.setVelocityX(settings.max_speed * (random() - 0.5))
    ship.setVelocityY(settings.max_speed * (random() - 0.5))
    state["ship"] = ship


def create_ufo():
    this = javascript.this()
    ufo = this.physics.add.sprite(window.innerWidth / 2, 200, "ufo")

    ufo.displayHeight = 100
    ufo.displayWidth = 100

    ufo.enableBody = True
    ufo.body.collideWorldBounds = True
    ufo.body.maxSpeed = settings.max_speed * settings.enemy_speed
    state["ufo"] = ufo


def create_score_counter():
    this = javascript.this()
    this.time.addEvent(
        {"delay": 1000, "loop": True, "callback": update_score}
    )


def update_score():
    state["score"] += 1
