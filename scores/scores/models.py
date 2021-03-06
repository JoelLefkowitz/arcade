import json
from dataclasses import dataclass


@dataclass
class Score:
    name: str
    value: int

    @property
    def json(self):
        return json.dumps(self.__dict__)
