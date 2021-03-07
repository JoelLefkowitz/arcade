from dataclasses import dataclass


@dataclass
class Settings:
    max_speed: int = 200
    max_acceleration: int = 100
    enemy_speed: float = 0.8
    enemy_acceleration: float = 0.9
