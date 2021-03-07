import javascript

from .main import settings, state


def handle_keys():
    ship = state.ship
    state.ufo

    javascript.this()
    cursors = this.input.keyboard.createCursorKeys()

    if cursors.left.isDown:
        ship.setAccelerationX(-settings.max_acceleration)

    elif cursors.right.isDown:
        ship.setAccelerationX(settings.max_acceleration)

    else:
        ship.setAccelerationX(0)

    if cursors.up.isDown:
        ship.setAccelerationY(-settings.max_acceleration)

    elif cursors.down.isDown:
        ship.setAccelerationY(settings.max_acceleration)

    else:
        ship.setAccelerationY(0)
