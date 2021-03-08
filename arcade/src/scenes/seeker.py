from math import pi
from random import random

import javascript
from browser import window
from scenes.base import BaseScene


class Seeker(BaseScene):
    key = "Seeker"
    score = 0

    ship = None
    ufo = None

    max_speed = 100
    max_acceleration = 20

    enemy_speed = 0.5
    enemy_acceleration = 0.7

    def preload(self):
        this = javascript.this()
        this.load.setBaseURL("./assets")
        this.load.image("ship", "ship.svg")
        this.load.image("ufo", "026-ufo.svg")

    def create(self, *args):
        this = javascript.this()
        self.create_ship(this)
        self.create_ufo(this)
        self.create_score_counter(this)

        this.physics.add.collider(
            self.ship, self.ufo, lambda *args: self.game_over(this)
        )

    def update(self, *args):
        this = javascript.this()
        self.handle_keys(this)
        self.ship.rotation = self.ship.body.angle + pi / 2

        self.ufo.setAccelerationX(
            (self.ship.x - self.ufo.x)
            * self.enemy_acceleration
            * random()
        )

        self.ufo.setAccelerationY(
            (self.ship.y - self.ufo.y)
            * self.enemy_acceleration
            * random()
        )

    def game_over(self, this):
        self.callback(self.score)
        this.scene.start("Menu")

    def handle_keys(self, this):
        cursors = this.input.keyboard.createCursorKeys()

        self.ship.setAccelerationX(
            -self.max_acceleration
            if cursors.left.isDown
            else self.max_acceleration
            if cursors.right.isDown
            else 0
        )

        self.ship.setAccelerationY(
            -self.max_acceleration
            if cursors.up.isDown
            else self.max_acceleration
            if cursors.down.isDown
            else 0
        )

    def create_ship(self, this):
        self.ship = this.physics.add.sprite(
            window.innerWidth / 2, window.innerHeight - 200, "ship"
        ).setOrigin(0.5)

        self.ship.displayHeight = 100
        self.ship.displayWidth = 100

        self.ship.enableBody = True
        self.ship.body.collideWorldBounds = True

        self.ship.setVelocityX(self.max_speed * (random() - 0.5))
        self.ship.setVelocityY(self.max_speed * (random() - 0.5))

        self.ship.body.maxSpeed = self.max_speed

    def create_ufo(self, this):
        self.ufo = this.physics.add.sprite(
            window.innerWidth / 2, 200, "ufo"
        ).setOrigin(0.5)

        self.ufo.displayHeight = 100
        self.ufo.displayWidth = 100

        self.ufo.enableBody = True
        self.ufo.body.collideWorldBounds = True

        self.ufo.body.maxSpeed = self.max_speed * self.enemy_speed

    def create_score_counter(self, this):
        this.time.addEvent(
            {
                "delay": 1000,
                "loop": True,
                "callback": self.increment_score,
            }
        )

    def increment_score(self):
        self.score += 1
