import random


class Environment(object):
    def __init__(self, name):
        self.name: str = name
        self.temperature: float = round(random.uniform(28, 30), 2)
        self.noise: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]
        self.light: bool = random.choices([True, False], [0.5, 0.5], k=1)[0]

    @property
    def __dict__(self):
        return {
            "name": self.name,
            "temperature": self.temperature,
            "noise": self.noise,
            "light": self.light,
        }
