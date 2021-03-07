from dataclasses import dataclass


@dataclass
class Score:
    name: str
    value: int

    @property
    def data(self):
        return self.__dict__
