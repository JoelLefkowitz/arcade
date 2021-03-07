from dataclasses import dataclass
from typing import Any


@dataclass
class State:
    ship: Any = None
    ufo: Any = None
    score: int = 0
