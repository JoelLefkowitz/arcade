import itertools
from math import pi
from random import random

import javascript
from base import BaseScene
from browser import window


class Seeker(BaseScene):
    key = "Seeker"

    ufo_svgs = [f"0{26 + i}-ufo.svg" for i in range(10)]
    scale = window.innerWidth / 15

    max_speed = 30
    max_acceleration = 300

    enemy_speed = 1.5
    enemy_acceleration = 0.3

    def preload(self):
        this = javascript.this()
        this.load.setBaseURL("./assets")
        this.load.image("ship", "ship.svg")

        self.ufo_sprites = []
        for i, svg in enumerate(self.ufo_svgs):
            self.ufo_sprites.append(f"ufo-{i}")
            this.load.image(f"ufo-{i}", svg)

    def create(self, *args):
        this = javascript.this()
        self.create_ship(this)
        self.create_ufos(this)
        self.create_score_counter(this)

        self.cursors = this.input.keyboard.createCursorKeys()

        self.cursors.left.isDown = False
        self.cursors.right.isDown = False
        self.cursors.up.isDown = False
        self.cursors.down.isDown = False

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

            if random() > (1 / 100):
                ufo.setVelocityX(
                    ufo.body.velocity.x
                    + self.max_speed
                    * self.enemy_speed
                    * (random() - 0.5)
                )
                ufo.setVelocityY(
                    ufo.body.velocity.y
                    + self.max_speed
                    * self.enemy_speed
                    * (random() - 0.5)
                )

    def game_over(self, this):
        self.callback(self.score)
        this.scene.start("Menu")

    def handle_keys(self, this):
        self.ship.setAccelerationX(
            -self.max_acceleration
            if self.cursors.left.isDown
            else self.max_acceleration
            if self.cursors.right.isDown
            else 0
        )

        self.ship.setAccelerationY(
            -self.max_acceleration
            if self.cursors.up.isDown
            else self.max_acceleration
            if self.cursors.down.isDown
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
        ufo_count = round(5 + 5 * random())
        ship_bounds = self.ship.getBounds()

        for i in range(ufo_count):
            ufo = this.physics.add.sprite(
                window.innerWidth * random(),
                window.innerHeight * random(),
                self.ufo_sprites[i % len(self.ufo_sprites)],
            ).setOrigin(0.5)

            ufo.displayHeight = self.scale
            ufo.displayWidth = self.scale

            ufo.enableBody = True
            ufo.body.collideWorldBounds = True

            ufo.body.maxSpeed = self.max_speed * self.enemy_speed

            ufo_bounds = ufo.getBounds()

            ship_overlap = window.Phaser.Geom.Intersects.GetRectangleIntersection(
                ufo_bounds, ship_bounds
            )

            if ship_overlap.height != 0 or ship_overlap.width != 0:
                ufo.destroy()
            else:
                self.ufos.append(ufo)

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
