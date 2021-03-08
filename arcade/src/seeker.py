import itertools
from math import pi
from random import random

import javascript
from browser import window
from base import BaseScene


class Seeker(BaseScene):
    key = "Seeker"
    ufo_count = 10

    scale = window.innerWidth / 15

    max_speed = 30
    max_acceleration = 300

    enemy_speed = 1.5
    enemy_acceleration = 0.3

    def preload(self):
        this = javascript.this()
        this.load.setBaseURL("./assets")
        this.load.image("ship", "ship.svg")

        self.ufo_imgs = []
        for i in range(10):
            self.ufo_imgs.append(f"ufo-{i}")
            this.load.image(f"ufo-{i}", f"0{26 + i}-ufo.svg")

    def create(self, *args):
        this = javascript.this()
        self.create_ship(this)
        self.create_ufos(this)
        self.create_score_counter(this)

        for ufo_i, ufo_j in itertools.combinations(self.ufos, 2):
            this.physics.add.collider(ufo_i, ufo_j)

        for ufo in self.ufos:
            this.physics.add.collider(
                self.ship, ufo, lambda *args: self.game_over(this)
            )

    def update(self, *args):
        this = javascript.this()
        self.handle_keys(this)
        self.ship.rotation = self.ship.body.angle + pi / 2

        for ufo in self.ufos:
            ufo.setAccelerationX(
                (self.ship.x - ufo.x)
                * self.enemy_acceleration
                * random()
            )

            ufo.setAccelerationY(
                (self.ship.y - ufo.y)
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

        self.ship.displayHeight = self.scale
        self.ship.displayWidth = self.scale

        self.ship.enableBody = True
        self.ship.body.collideWorldBounds = True

        self.ship.setVelocityX(self.max_speed * (random() - 0.5))
        self.ship.setVelocityY(self.max_speed * (random() - 0.5))

        self.ship.body.maxSpeed = self.max_speed

    def create_ufos(self, this):
        self.ufos = []

        for i in range(self.ufo_count):
            ufo = this.physics.add.sprite(
                window.innerWidth * random(),
                window.innerHeight * random(),
                self.ufo_imgs[i % len(self.ufo_imgs)],
            ).setOrigin(0.5)

            self.ufos.append(ufo)

            ufo.displayHeight = self.scale
            ufo.displayWidth = self.scale

            ufo.enableBody = True
            ufo.body.collideWorldBounds = True

            ufo.body.maxSpeed = self.max_speed * self.enemy_speed

    def create_score_counter(self, this):
        self.score = 0
        this.time.addEvent(
            {
                "delay": 1000,
                "loop": True,
                "callback": self.increment_score,
            }
        )

    def increment_score(self):
        self.score += 1
